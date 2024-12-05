from sqlalchemy.orm import Session
from models.asset_model import Asset
from models.user_model import User
from schema.schema import SignupSchema, LoginSchema, AssetSchema

from fastapi import status, HTTPException


async def create_user(db: Session, user: SignupSchema):
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    return new_user


async def get_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


async def login_user(db: Session, user: LoginSchema):
    user = db.query(User).filter(User.email == user.email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


async def create_asset(db: Session, asset: AssetSchema):
    new_asset = Asset(**asset.dict())
    db.add(new_asset)
    db.commit()
    return new_asset


async def get_asset(db: Session, asset_id: int):
    asset = db.query(Asset).filter(Asset.id == asset_id).first()
    if asset is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Asset not found")
    return asset
