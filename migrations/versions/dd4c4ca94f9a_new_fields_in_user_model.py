"""new fields in user model

Revision ID: dd4c4ca94f9a
Revises: 47fe8e32b600
Create Date: 2020-06-12 11:45:22.656431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd4c4ca94f9a'
down_revision = '47fe8e32b600'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'body',
               existing_type=sa.VARCHAR(length=140),
               nullable=False)
    op.add_column('user', sa.Column('about', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('user', 'password_hash',
               existing_type=sa.VARCHAR(length=128),
               nullable=False)
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    op.alter_column('user', 'password_hash',
               existing_type=sa.VARCHAR(length=128),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about')
    op.alter_column('post', 'body',
               existing_type=sa.VARCHAR(length=140),
               nullable=True)
    # ### end Alembic commands ###
