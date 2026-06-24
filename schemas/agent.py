from pydantic import (
    BaseModel,
    EmailStr
)


class AgentCreate(BaseModel):

    name: str

    email: EmailStr

    department: str
