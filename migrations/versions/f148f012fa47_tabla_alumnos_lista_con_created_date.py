"""tabla alumnos lista con created_date

Revision ID: f148f012fa47
Revises: 48f93db644cc
Create Date: 2026-03-26 08:39:24.561899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f148f012fa47'
down_revision = '48f93db644cc'
branch_labels = None
depends_on = None


def upgrade():
    # Migration vacía - created_date ya existe en la tabla alumnos
    pass


def downgrade():
    # No hacer nada en downgrade
    pass
