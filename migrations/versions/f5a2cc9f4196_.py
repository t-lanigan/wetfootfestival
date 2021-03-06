"""empty message

Revision ID: f5a2cc9f4196
Revises:
Create Date: 2020-06-28 21:25:40.670813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5a2cc9f4196'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'email',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=False)
    op.alter_column('artists', 'name',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=False)
    op.alter_column('artists', 'phone_number',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=False)
    op.alter_column('events', 'email',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=False)
    op.alter_column('events', 'name',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=False)
    op.alter_column('events', 'phone_number',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=False)
    op.alter_column('volunteers', 'email',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=False)
    op.alter_column('volunteers', 'name',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=False)
    op.alter_column('volunteers', 'phone_number',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('volunteers_name_key', 'volunteers', ['name'])
    op.alter_column('volunteers', 'phone_number',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=True)
    op.alter_column('volunteers', 'name',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=True)
    op.alter_column('volunteers', 'email',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=True)
    op.create_unique_constraint('events_name_key', 'events', ['name'])
    op.alter_column('events', 'phone_number',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=True)
    op.alter_column('events', 'name',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=True)
    op.alter_column('events', 'email',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=True)
    op.create_unique_constraint('artists_name_key', 'artists', ['name'])
    op.alter_column('artists', 'phone_number',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=True)
    op.alter_column('artists', 'name',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=True)
    op.alter_column('artists', 'email',
                    existing_type=sa.VARCHAR(length=120),
                    nullable=True)
    # ### end Alembic commands ###
