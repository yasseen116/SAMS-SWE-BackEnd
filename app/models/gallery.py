"""Gallery media ORM model placeholder."""

from sqlalchemy import Column, Integer, String, Text, DateTime

from .base import Base


class GalleryItem(Base):
    """
    Represents images/media shown in the gallery.
    TODO: add id, title/caption, media_url, alt_text, uploaded_at, created_by metadata.
    """

    __tablename__ = "gallery_items"

    # Example columns to add during implementation:
    # id = Column(Integer, primary_key=True, index=True)
    # title = Column(String(255))
    # description = Column(Text)
    # media_url = Column(String(512), nullable=False)
    # uploaded_at = Column(DateTime(timezone=True))
    pass
