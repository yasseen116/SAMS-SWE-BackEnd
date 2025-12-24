"""College staff (doctors) ORM model placeholder."""

from sqlalchemy import Column, Integer, String, Text

from .base import Base


class StaffMember(Base):
    """
    Represents faculty/staff members.
    TODO: add id, name, title, photo_url, qualifications, specialties, contact info, office hours fields.
    """

    __tablename__ = "staff_members"

    # Example columns to add during implementation:
    # id = Column(Integer, primary_key=True, index=True)
    # name = Column(String(255), nullable=False)
    # title = Column(String(255))
    # photo_url = Column(String(512))
    # bio = Column(Text)
    pass
