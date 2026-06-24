from pydantic import BaseModel


class ResolutionCreate(BaseModel):

    resolution_note: str

    resolved_by: str
