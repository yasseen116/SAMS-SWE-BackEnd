"""Authentication/administrators ORM model placeholder."""

from sqlalchemy import Column, Integer, String, Boolean, DateTime

from .base import Base


class AdminUser(Base):
    """
    Represents authenticated administrative users.
    TODO: add id, username/email, hashed_password, role, is_active, created_at/updated_at fields.
    """

    __tablename__ = "admin_users"

    # Example columns to add during implementation:
    # id = Column(Integer, primary_key=True, index=True)
    # email = Column(String(255), unique=True, nullable=False, index=True)
    # hashed_password = Column(String(255), nullable=False)
    # is_active = Column(Boolean, default=True)
    # created_at = Column(DateTime(timezone=True))
    pass
