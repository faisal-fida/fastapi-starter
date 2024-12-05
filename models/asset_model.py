from sqlalchemy import Column, Integer, String, DateTime, Boolean
from . import Base
from typing import Any
from utils.utility import to_dict


class Asset(Base):
    __tablename__ = "asset"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    category = Column(String)
    date = Column(DateTime)
    eligible = Column(Boolean, nullable=True)
    zakatRate = Column(Integer, nullable=True)
    amount = Column(Integer)

    def dict(self) -> dict[str, Any]:
        return to_dict(self)
