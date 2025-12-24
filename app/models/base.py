"""SQLAlchemy declarative base."""

from sqlalchemy.orm import declarative_base

# Use this Base for all ORM models; configure engine/session when wiring persistence.
Base = declarative_base()
