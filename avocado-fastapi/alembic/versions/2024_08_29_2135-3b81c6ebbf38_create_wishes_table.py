"""create wishes table

Revision ID: 3b81c6ebbf38
Revises: 974ac9cbeba5
Create Date: 2024-08-29 21:35:01.222256

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3b81c6ebbf38"
down_revision: Union[str, None] = "974ac9cbeba5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "wish",
        sa.Column("title", sa.String(length=100), nullable=False),
        sa.Column("body", sa.Text(), nullable=False),
        sa.Column("holiday", sa.String(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"], ["user.id"], name=op.f("fk_wish_user_id_user")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_wish")),
    )


def downgrade() -> None:
    op.drop_table("wish")
