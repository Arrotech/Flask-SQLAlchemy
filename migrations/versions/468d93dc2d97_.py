"""empty message

Revision ID: 468d93dc2d97
Revises: b0f39f194352
Create Date: 2020-03-18 03:54:50.244003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '468d93dc2d97'
down_revision = 'b0f39f194352'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'hashed_psw')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hashed_psw', sa.VARCHAR(length=128), nullable=True))
    # ### end Alembic commands ###
