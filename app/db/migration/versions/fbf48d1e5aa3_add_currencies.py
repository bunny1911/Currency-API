"""
add currencies

Revision ID: fbf48d1e5aa3
Revises: 74a7aa7156ea
Create Date: 2022-09-17 19:06:39.784460
"""

from alembic import op
from app.scripts import get_currencies


# revision identifiers, used by Alembic.
revision = 'fbf48d1e5aa3'
down_revision = '74a7aa7156ea'
branch_labels = None
depends_on = None


def upgrade() -> None:
    get_currencies()


def downgrade() -> None:
    op.execute(
        """
        TRUNCATE TABLE currency
        RESTART IDENTITY CASCADE;
        """
    )
