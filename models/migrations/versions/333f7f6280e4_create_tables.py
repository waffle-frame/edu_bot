"""create tables

Revision ID: 333f7f6280e4
Revises: 
Create Date: 2022-12-04 00:45:13.727737

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '333f7f6280e4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    OCCUPATION_TYPES = [
        ("Групповые", "Групповые"),
        ("Индивидуальные", "Индивидуальные"),
    ]

    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('username', sa.VARCHAR(length=20), nullable=True),
    sa.Column('userbot', sa.String(), nullable=False),
    sa.Column('group_title', sa.VARCHAR(length=20), nullable=False),
    sa.Column('occupation_type', sqlalchemy_utils.types.choice.ChoiceType(OCCUPATION_TYPES), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('groups')
    # ### end Alembic commands ###
