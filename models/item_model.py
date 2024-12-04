from sqlalchemy import Column, Integer, String
from . import Base
from typing import Any
from utils.utility import to_dict


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String)

    def dict(self) -> dict[str, Any]:
        return to_dict(self)
