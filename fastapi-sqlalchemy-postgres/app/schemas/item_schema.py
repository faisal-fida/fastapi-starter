from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    title: str | None = None
    description: str | None = None

class ItemInDB(ItemBase):
    id: int
    class Config:
        from_attributes = True