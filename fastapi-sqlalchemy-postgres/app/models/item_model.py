from sqlalchemy import Column, Integer, String
from . import Base
from typing import Any

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    description = Column(String)

    def dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the model instance.

        Includes all attributes defined on the model class.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}