from pydantic import BaseModel


class SignupSchema(BaseModel):
    name: str
    email: str
    password: str
    role: str
    assetID: str


class LoginSchema(BaseModel):
    email: str
    password: str


class AssetSchema(BaseModel):
    name: str
    category: str
    date: str
    eligible: bool
    zakatRate: int
