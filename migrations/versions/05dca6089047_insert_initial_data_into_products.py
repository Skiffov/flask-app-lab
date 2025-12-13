"""insert initial data into products

Revision ID: 05dca6089047
Revises: 3cf7147640e6
Create Date: 2025-12-13 20:42:53.585050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05dca6089047'
down_revision = '3cf7147640e6'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        "INSERT INTO category (name) VALUES ('Electronics'), ('Books')"
    )

    op.execute(
        """
        INSERT INTO product (name, price, category_id, created_at)
        VALUES
        ('Laptop', 1200, 1, CURRENT_TIMESTAMP),
        ('Python Book', 40, 2, CURRENT_TIMESTAMP)
        """
    )


def downgrade():
    op.execute("DELETE FROM product")
    op.execute("DELETE FROM category")


    # ### end Alembic commands ###
