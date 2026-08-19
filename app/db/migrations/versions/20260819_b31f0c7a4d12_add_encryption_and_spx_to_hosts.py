"""add encryption and reality spiderX to hosts

Revision ID: b31f0c7a4d12
Revises: 57eba0a293f2
Create Date: 2026-08-19 23:45:00.000000

VLESS Encryption (xray >= v25.9.5) is normally derived from the inbound, the
same way the REALITY public key is. This column only exists so an operator can
override that per host, e.g. while migrating keys.

Text rather than String because an ML-KEM-768 client key is 1184 bytes, which
is ~1580 base64 characters before the prefix, and the format allows chaining
several of them.
"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "b31f0c7a4d12"
down_revision = "57eba0a293f2"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("hosts", sa.Column("encryption", sa.Text(), nullable=True))
    op.add_column(
        "hosts", sa.Column("reality_spx", sa.String(length=256), nullable=True)
    )


def downgrade() -> None:
    op.drop_column("hosts", "reality_spx")
    op.drop_column("hosts", "encryption")
