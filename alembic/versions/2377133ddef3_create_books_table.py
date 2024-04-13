"""create books table

Revision ID: 2377133ddef3
Revises:
Create Date: 2024-04-14 01:23:44.255725

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2377133ddef3"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "books",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("book_name", sa.String),
        sa.Column("author", sa.String),
    )


def downgrade() -> None:
    op.drop_table("books")
