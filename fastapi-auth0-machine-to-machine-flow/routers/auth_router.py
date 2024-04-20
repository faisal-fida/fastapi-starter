from fastapi import APIRouter
from ..services.auth_service import AuthService
from ..schema.auth_schema import SignupSchema, LoginSchema

router = APIRouter()


@router.get("/health_check")
def health_check():
    return {"msg": "Welcome to auth service"}


@router.post("/create_user")
async def create_user(user: SignupSchema):
    return await AuthService.create_user(user)


@router.post("/login_user")
async def login_user(user: LoginSchema):
    return await AuthService.login_user(user)
