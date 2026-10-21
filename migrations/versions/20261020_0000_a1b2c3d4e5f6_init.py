"""init

Пустая начальная ревизия: проверяет, что миграции применяются.
Схему БД добавьте следующими ревизиями.

Revision ID: a1b2c3d4e5f6
Revises:
Create Date: 2026-10-20 00:00:00

"""

from collections.abc import Sequence

revision: str = "a1b2c3d4e5f6"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
