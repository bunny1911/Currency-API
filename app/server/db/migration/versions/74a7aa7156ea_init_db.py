"""
Init db

Revision ID: 74a7aa7156ea
Revises: 
Create Date: 2022-09-17 15:03:19.208551
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "74a7aa7156ea"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "currency",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("code", sa.VARCHAR(length=3), nullable=False),
        sa.Column("title", sa.VARCHAR(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("code")
    )

    op.create_table(
        "rate",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("currency_id", sa.INTEGER(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column("value", sa.NUMERIC(precision=10, scale=4), nullable=False),
        sa.ForeignKeyConstraint(("currency_id", ), ["currency.id"], ),
        sa.PrimaryKeyConstraint("id")
    )


def downgrade() -> None:
    op.drop_table("rate")
    op.drop_table("currency")
