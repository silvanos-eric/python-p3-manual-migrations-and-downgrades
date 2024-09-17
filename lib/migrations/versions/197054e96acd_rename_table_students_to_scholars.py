"""Rename table students to scholars

Revision ID: 197054e96acd
Revises: 791279dd0760
Create Date: 2024-09-17 16:32:36.291339

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '197054e96acd'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
