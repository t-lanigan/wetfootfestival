import json
from flask import request, _request_ctx_stack
from functools import wraps
from jose import jwt
from urllib.request import urlopen


AUTH0_DOMAIN = 'tylers-test.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'wetfootfestival'

# https://tylers-test.auth0.com/authorize?audience=wetfootfestival&response_type=token&client_id=LFlinn4YCy2LNnJdzw6c0k2uOwl59nKH&redirect_uri=https://wetfootfestival.herokuapp.com/login-results
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhUUWJaTlZnYzVMVFVxdHFzU2t2YyJ9.eyJpc3MiOiJodHRwczovL3R5bGVycy10ZXN0LmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNzM5NDcwMTI4MjUzNTgyNTk1OSIsImF1ZCI6WyJ3ZXRmb290ZmVzdGl2YWwiLCJodHRwczovL3R5bGVycy10ZXN0LmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTM1ODMxMzAsImV4cCI6MTU5MzU5MDMzMCwiYXpwIjoiTEZsaW5uNFlDeTJMTm5KZHp3NmMwazJ1T3dsNTluS0giLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiYWZmZWN0OmFydGlzdHMiLCJhZmZlY3Q6ZXZlbnRzIiwiYWZmZWN0OnZvbHVudGVlcnMiLCJnZXQ6aXRlbXMiXX0.pV3qrTXAgrdOVkLKESekaSxmwYZWqSRSAWfj7Im27uyyuAk5keccAQ34xWxP45_Jr08zO1tlh0bfSdoP58V2t4Oev5EkKICDFmQQGdpo7aNupxCZWlFIjYuJG8hX7_rvpfio5OrUR8PhRLTV6ID5vDHKywb9QbcxikW1r9b87_o-sjNog-BOTF0-bvXqm-hqG5CZTMkKtToY25f8BHgh2CZBxVSuysB6ElXCNj5L-p0SgRkv3nS5_72vJgJEI34Ja13pJoxPykUJp9YxDW7DAUbeX3oESAQmTNTAN3sVBoJJqAi9qaUMnypAdwsau0VR5IKkXLOlYbbGxx7eiFye_A

class AuthError(Exception):
    """A standardized way to communicate auth failure modes
    Extends: Exception
    """

    def __init__(self, error, status_code):
        """Initialized a Auth Error.
        Arguments:
            error str -- A message giving specifics about the error.
            status_code int -- The status code error
        """
        self.error = error
        self.status_code = status_code


def get_token_auth_header():
    """Attempts to get the header from the request and
    to split bearer and the token.
    Raises:
        AuthError: if no header is present
        AuthError: if the header is malformed
        AuthError: if there is not bearer is header
    Returns:
        str -- the token part of the header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({
            "code": "authorization_header_missing",
            "description": "Authorization header is expected."
        }, 401)

    parts = auth.split()
    if parts[0].lower() != "bearer":
        raise AuthError({
            "code": "invalid_header",
            "description": "Authorization header must start with 'Bearer'."
        }, 401)

    elif len(parts) == 1:
        raise AuthError({
            "code": "invalid_header",
            "description": "Token not found."
        }, 401)

    elif len(parts) > 2:
        raise AuthError({
            "code": "invalid_header",
            "description": "Authorization header must be bearer token."
        }, 401)

    token = parts[1]
    return token


def check_permissions(permission, payload):
    """Checks if the required permission is in the payload.
    Arguments:
        permission str -- the permissions string being sought after (e.g get:drinks)
        payload dict -- the payload
    Raises:
        AuthError: if permissions are not included in the payload
        AuthError: if the requested permission string is not in the payload permissions array
    Returns:
        boolean -- true, false
    """
    if "permissions" not in payload:
        raise AuthError({
            "code": "invalid_header",
            "description": "Permissions not included in payload."
        }, 400)
    if permission not in payload["permissions"]:
        raise AuthError({
            "code": "unauthorized",
            "description": "Permission not found."
        }, 403)
    return True


'''
!!NOTE urlopen has a common certificate error described here: 
https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org
'''


def verify_decode_jwt(token):
    """verify the token using Auth0 /.well-known/jwks.json
    Arguments:
        token str -- jwt token
    Raises:
        AuthError: if "kid" not in unverified_header
        AuthError: if token is expired
        AuthError: if there are incorrect claims
        AuthError: [if it unable to parse the token
        AuthError: if it's unable to find appropriate key
    """
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
    raise AuthError({
        'code': 'invalid_header',
                'description': 'Unable to find the appropriate key.'
    }, 400)


def requires_auth(permission=''):
    """A decorator used to require permissions for a path. 
    Example usage: @requires_auth('get:drinks')
    Keyword Arguments:
        permission {str} -- The required permission (default: {''})
    """
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper
    return requires_auth_decorator