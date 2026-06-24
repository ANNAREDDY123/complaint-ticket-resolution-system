from pydantic import BaseModel


class ComplaintCreate(BaseModel):

    title: str

    description: str

    category: str

    priority: str

    status: str = "Open"
