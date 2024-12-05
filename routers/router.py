from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.service import get_asset, create_asset, get_user, create_user, login_user
from schema.schema import AssetSchema, SignupSchema, LoginSchema
from utils.database import get_db

router = APIRouter()


@router.get("/{asset_id}", response_model=AssetSchema)
async def get_asset_handler(asset_id: int, db: Session = Depends(get_db)):
    return await get_asset(db=db, asset_id=asset_id)


@router.post("/asset", response_model=AssetSchema)
async def create_asset_handler(asset: AssetSchema, db: Session = Depends(get_db)):
    return await create_asset(db=db, asset=asset)


@router.get("/user/{user_id}", response_model=SignupSchema)
async def get_user_handler(user_id: int, db: Session = Depends(get_db)):
    return await get_user(db=db, user_id=user_id)


@router.post("/user", response_model=SignupSchema)
async def create_user_handler(user: SignupSchema, db: Session = Depends(get_db)):
    return await create_user(db=db, user=user)


@router.post("/login", response_model=LoginSchema)
async def login_user_handler(user: LoginSchema, db: Session = Depends(get_db)):
    return await login_user(db=db, user=user)
