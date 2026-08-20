"""widen inbounds.config

Revision ID: c74a1e5b9f30
Revises: b31f0c7a4d12
Create Date: 2026-08-20 07:55:00.000000

String(512) was already tight and the post-quantum key material pushes well
past it: a REALITY inbound advertising mldsa65Verify serialises to ~3.3 kB and
a VLESS Encryption inbound to ~1.9 kB. MySQL rejects the write outright with
"Data too long for column 'config'", and because the panel swallowed sync
errors the node simply stayed 'unhealthy: timeout' with no explanation.
"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c74a1e5b9f30"
down_revision = "b31f0c7a4d12"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        "inbounds",
        "config",
        existing_type=sa.String(length=512),
        type_=sa.Text(),
        existing_nullable=False,
    )


def downgrade() -> None:
    op.alter_column(
        "inbounds",
        "config",
        existing_type=sa.Text(),
        type_=sa.String(length=512),
        existing_nullable=False,
    )
