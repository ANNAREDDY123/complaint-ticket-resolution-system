from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

from datetime import datetime

from database import Base


class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(
        Integer,
        primary_key=True
    )

    title = Column(String)

    description = Column(String)

    category = Column(String)

    priority = Column(String)

    status = Column(
        String,
        default="Open"
    )

    agent_id = Column(
        Integer,
        ForeignKey("agents.id"),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
