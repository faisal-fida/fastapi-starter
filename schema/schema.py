from pydantic import BaseModel


class SignupSchema(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str
    phoneNumber: str
    role: str


class LoginSchema(BaseModel):
    email: str
    password: str


class AssetSchema(BaseModel):
    name: str
    category: str
    date: str
    eligible: bool
    zakatRate: int
