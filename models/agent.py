from sqlalchemy import (
    Column,
    Integer,
    String
)

from database import Base


class Agent(Base):
    __tablename__ = "agents"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(String)

    email = Column(
        String,
        unique=True
    )

    department = Column(String)
