from pydantic import BaseModel, EmailStr, validator


class SignupSchema(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str
    phoneNumber: str
    NMLS: str
    lenderId: int


class LoginSchema(BaseModel):
    email: str
    password: str
