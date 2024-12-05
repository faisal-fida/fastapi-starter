from pydantic import BaseModel
from datetime import datetime


class SignupSchema(BaseModel):
    name: str
    email: str
    password: str
    role: str
    assetID: int


class LoginSchema(BaseModel):
    email: str
    password: str


class AssetSchema(BaseModel):
    name: str
    category: str
    date: datetime
    eligible: bool
    zakatRate: int
    amount: int
