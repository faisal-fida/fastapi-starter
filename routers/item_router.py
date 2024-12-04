from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.item_service import create_item, get_item
from schema.item_schema import ItemCreate, ItemInDB
from utils.database import get_db

router = APIRouter()


@router.post("/", response_model=ItemInDB)
async def create_item_handler(item: ItemCreate, db: Session = Depends(get_db)):
    return await create_item(db=db, item=item)


@router.get("/{item_id}", response_model=ItemInDB)
async def get_item_handler(item_id: int, db: Session = Depends(get_db)):
    return await get_item(db=db, item_id=item_id)
