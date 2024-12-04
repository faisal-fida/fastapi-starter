from pydantic import BaseModel


class SignupSchema(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str
    phoneNumber: str


class LoginSchema(BaseModel):
    email: str
    password: str
