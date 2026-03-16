from alembic import op
import sqlalchemy as sa

revision = "1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "items",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("value", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
    )
    op.create_index("ix_items_id", "items", ["id"], unique=False)
    op.create_index("ix_items_name", "items", ["name"], unique=False)


def downgrade():
    op.drop_index("ix_items_name", table_name="items")
    op.drop_index("ix_items_id", table_name="items")
    op.drop_table("items")