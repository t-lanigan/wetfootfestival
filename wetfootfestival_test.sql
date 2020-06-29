--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3
-- Dumped by pg_dump version 12.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: tyler
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO tyler;

--
-- Name: artists; Type: TABLE; Schema: public; Owner: tyler
--

CREATE TABLE public.artists (
    id integer NOT NULL,
    name character varying(120) NOT NULL,
    phone_number character varying(120) NOT NULL,
    email character varying(120) NOT NULL,
    event integer NOT NULL,
    website character varying(200),
    instagram_link character varying(500),
    image_link character varying(500)
);


ALTER TABLE public.artists OWNER TO tyler;

--
-- Name: artists_id_seq; Type: SEQUENCE; Schema: public; Owner: tyler
--

CREATE SEQUENCE public.artists_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.artists_id_seq OWNER TO tyler;

--
-- Name: artists_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tyler
--

ALTER SEQUENCE public.artists_id_seq OWNED BY public.artists.id;


--
-- Name: events; Type: TABLE; Schema: public; Owner: tyler
--

CREATE TABLE public.events (
    id integer NOT NULL,
    name character varying(120) NOT NULL,
    phone_number character varying(120) NOT NULL,
    email character varying(120) NOT NULL,
    venue_name character varying NOT NULL,
    theme character varying NOT NULL,
    website character varying(200)
);


ALTER TABLE public.events OWNER TO tyler;

--
-- Name: events_id_seq; Type: SEQUENCE; Schema: public; Owner: tyler
--

CREATE SEQUENCE public.events_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.events_id_seq OWNER TO tyler;

--
-- Name: events_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tyler
--

ALTER SEQUENCE public.events_id_seq OWNED BY public.events.id;


--
-- Name: volunteers; Type: TABLE; Schema: public; Owner: tyler
--

CREATE TABLE public.volunteers (
    id integer NOT NULL,
    name character varying(120) NOT NULL,
    phone_number character varying(120) NOT NULL,
    email character varying(120) NOT NULL,
    event integer NOT NULL
);


ALTER TABLE public.volunteers OWNER TO tyler;

--
-- Name: volunteers_id_seq; Type: SEQUENCE; Schema: public; Owner: tyler
--

CREATE SEQUENCE public.volunteers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.volunteers_id_seq OWNER TO tyler;

--
-- Name: volunteers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tyler
--

ALTER SEQUENCE public.volunteers_id_seq OWNED BY public.volunteers.id;


--
-- Name: artists id; Type: DEFAULT; Schema: public; Owner: tyler
--

ALTER TABLE ONLY public.artists ALTER COLUMN id SET DEFAULT nextval('public.artists_id_seq'::regclass);


--
-- Name: events id; Type: DEFAULT; Schema: public; Owner: tyler
--

ALTER TABLE ONLY public.events ALTER COLUMN id SET DEFAULT nextval('public.events_id_seq'::regclass);


--
-- Name: volunteers id; Type: DEFAULT; Schema: public; Owner: tyler
--

ALTER TABLE ONLY public.volunteers ALTER COLUMN id SET DEFAULT nextval('public.volunteers_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: tyler
--

COPY public.alembic_version (version_num) FROM stdin;
f5a2cc9f4196
\.


--
-- Data for Name: artists; Type: TABLE DATA; Schema: public; Owner: tyler
--

COPY public.artists (id, name, phone_number, email, event, website, instagram_link, image_link) FROM stdin;
1	Justin Beiberlake	555-555-5556	jbl@gmail.com	1	https://www.youtube.com/watch?v=dQw4w9WgXcQ	https://www.facebook.com/joeexotic	https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80
2	Gnarfunkel	555-555-5557	gnarfunkelband@gmail.com	1	https://www.youtube.com/watch?v=dQw4w9WgXcQ	https://www.facebook.com/joeexotic	https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80
\.


--
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: tyler
--

COPY public.events (id, name, phone_number, email, venue_name, theme, website) FROM stdin;
1	Wetfoot Festival 2019	555-555-5555	wisehall@gmail.com	The Wisehall	Major Tom Goes to Wonderland	https://www.youtube.com/watch?v=dQw4w9WgXcQ
\.


--
-- Data for Name: volunteers; Type: TABLE DATA; Schema: public; Owner: tyler
--

COPY public.volunteers (id, name, phone_number, email, event) FROM stdin;
1	Tyler	555-555-5558	tyler@gmail.com	1
2	Annie	555-555-5559	annie@gmail.com	1
\.


--
-- Name: artists_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tyler
--

SELECT pg_catalog.setval('public.artists_id_seq', 2, true);


--
-- Name: events_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tyler
--

SELECT pg_catalog.setval('public.events_id_seq', 1, true);


--
-- Name: volunteers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: tyler
--

SELECT pg_catalog.setval('public.volunteers_id_seq', 2, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: tyler
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: artists artists_email_key; Type: CONSTRAINT; Schema: public; Owner: tyler
--

ALTER TABLE ONLY public.artists
    ADD CONSTRAINT artists_email_key UNIQUE (email);


--
-- Name: artists artists_phone_number_key; Type: CONSTRAINT; Schema: public; Owner: tyler
--

ALTER TABLE ONLY public.artists
    ADD CONSTRAINT artists_phone_number_key UNIQUE (phone_number);


--
-- Name: artists artists_pkey; Type: CONSTRAINT; Schema: public; Owner: tyler
--

ALTER TABLE ONLY public.artists
    ADD CONSTRAINT artists_pkey PRIMARY KEY (id);


--
-- Name: events events_email_key; Type: CONSTRAINT; Schema: public; Owner: tyler
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_email_key UNIQUE (email);


--
-- Name: events events_phone_number_key; Type: CONSTRAINT; Schema: public; Owner: tyler
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_phone_number_key UNIQUE (phone_number);


--
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: tyler
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (id);


--
-- Name: volunteers volunteers_email_key; Type: CONSTRAINT; Schema: public; Owner: tyler
--

ALTER TABLE ONLY public.volunteers
    ADD CONSTRAINT volunteers_email_key UNIQUE (email);


--
-- Name: volunteers volunteers_phone_number_key; Type: CONSTRAINT; Schema: public; Owner: tyler
--

ALTER TABLE ONLY public.volunteers
    ADD CONSTRAINT volunteers_phone_number_key UNIQUE (phone_number);


--
-- Name: volunteers volunteers_pkey; Type: CONSTRAINT; Schema: public; Owner: tyler
--

ALTER TABLE ONLY public.volunteers
    ADD CONSTRAINT volunteers_pkey PRIMARY KEY (id);


--
-- Name: artists artists_event_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tyler
--

ALTER TABLE ONLY public.artists
    ADD CONSTRAINT artists_event_fkey FOREIGN KEY (event) REFERENCES public.events(id);


--
-- Name: volunteers volunteers_event_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tyler
--

ALTER TABLE ONLY public.volunteers
    ADD CONSTRAINT volunteers_event_fkey FOREIGN KEY (event) REFERENCES public.events(id);


--
-- PostgreSQL database dump complete
--

