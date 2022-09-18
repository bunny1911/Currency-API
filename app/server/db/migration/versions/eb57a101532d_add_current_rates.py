"""
add current rates

Revision ID: eb57a101532d
Revises: fbf48d1e5aa3
Create Date: 2022-09-18 15:55:30.518558
"""

from alembic import op
from app.server.scripts import get_rates


# revision identifiers, used by Alembic.
revision = 'eb57a101532d'
down_revision = 'fbf48d1e5aa3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    get_rates(currencies=["EUR", "UAH"])


def downgrade() -> None:
    op.execute(
        """
        TRUNCATE TABLE currency
        RESTART IDENTITY CASCADE;
        """
    )
