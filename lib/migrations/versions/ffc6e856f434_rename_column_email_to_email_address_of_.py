"""Rename column `email` to `email_address` of students table

Revision ID: ffc6e856f434
Revises: 7112ef2702a9
Create Date: 2024-09-17 17:00:14.435662

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ffc6e856f434'
down_revision = '7112ef2702a9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'email', new_column_name='email_address')


def downgrade() -> None:
    op.alter_column('students', 'email_address', new_column_name='email')
