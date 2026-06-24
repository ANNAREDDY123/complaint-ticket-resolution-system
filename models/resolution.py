from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from datetime import datetime

from database import Base


class Resolution(Base):
    __tablename__ = "resolutions"

    id = Column(
        Integer,
        primary_key=True
    )

    ticket_id = Column(
        Integer,
        ForeignKey("complaints.id")
    )

    resolution_note = Column(String)

    resolved_by = Column(String)

    resolved_at = Column(
        DateTime,
        default=datetime.utcnow
    )
