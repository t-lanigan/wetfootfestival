from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app
from models import db

migrate = Migrate(app, db)
manager = Manager(app)

# TODO: Understand why this works weird (first time running migrate doesn't seem to generate
# the correct version file)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
