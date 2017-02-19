from alembic import op
import sqlalchemy as sa


revision = '114a1955ff9c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('document', sa.Column('readonly', sa.Boolean))


def downgrade():
    pass
