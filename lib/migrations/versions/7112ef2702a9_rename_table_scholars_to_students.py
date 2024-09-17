"""Rename table scholars to students

Revision ID: 7112ef2702a9
Revises: 197054e96acd
Create Date: 2024-09-17 16:48:58.153464

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '7112ef2702a9'
down_revision = '197054e96acd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('scholars', 'students')


def downgrade() -> None:
    op.rename_table('students', 'scholars')
