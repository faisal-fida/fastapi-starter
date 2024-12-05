from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base
from typing import Any
from utils.utility import to_dict
from models.asset_model import Asset


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String)
    password = Column(String)
    role = Column(String)
    assetID = Column(Integer, ForeignKey(Asset.id), nullable=True)

    asset = relationship("Asset", foreign_keys="User.assetID")

    def dict(self) -> dict[str, Any]:
        return to_dict(self)
