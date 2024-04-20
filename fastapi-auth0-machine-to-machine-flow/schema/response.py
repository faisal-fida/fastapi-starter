from pydantic import BaseModel
from typing import Optional

class ResponseSchema(BaseModel):
    status: int
    message: str
    success: bool
    data: Optional[object] = {}
