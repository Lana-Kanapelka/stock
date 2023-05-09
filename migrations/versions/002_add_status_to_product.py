"""Add status to product

Revision ID: 002
Revises: 
Create Date: 2023-05-05 18:24:59.501485

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '002'
down_revision = "001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("CREATE TYPE product_status AS ENUM('PENDING', 'ACTIVE', 'BANED', 'SOLD')")
    op.execute((
        "ALTER TABLE IF EXISTS product "
        "ADD COLUMN status product_status DEFAULT 'ACTIVE'"
    ))


def downgrade() -> None:
    op.execute(
        "ALTER TABLE IF EXISTS product "
        "DROP COLUMN status"
    )
    op.execute("DROP TYPE IF EXISTS product_status")
