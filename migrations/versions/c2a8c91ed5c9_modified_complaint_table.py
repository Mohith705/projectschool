"""modified complaint table

Revision ID: c2a8c91ed5c9
Revises: 8a84cfd9ea0e
Create Date: 2024-12-20 20:21:57.442589

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'c2a8c91ed5c9'
down_revision: Union[str, None] = '8a84cfd9ea0e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('complaintable', sa.Column('complaintdate', sa.Date(), nullable=False))
    op.drop_column('complaintable', 'complaindate')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('complaintable', sa.Column('complaindate', sa.DATE(), autoincrement=False, nullable=False))
    op.drop_column('complaintable', 'complaintdate')
    # ### end Alembic commands ###
