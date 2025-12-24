"""Announcement ORM model placeholder."""

from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean

from .base import Base


class Announcement(Base):
    """
    Represents public announcements.
    TODO: add id, title, body/content, published_at, is_active, created_at timestamps, and indexing.
    """

    __tablename__ = "announcements"

    # Example columns to add during implementation:
    # id = Column(Integer, primary_key=True, index=True)
    # title = Column(String(255), nullable=False)
    # body = Column(Text, nullable=False)
    # published_at = Column(DateTime(timezone=True))
    # is_active = Column(Boolean, default=True)
    pass
