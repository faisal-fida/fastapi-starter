from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.item_service import create_item, get_item
from app.models.item_model import Item
from app.schemas.item_schema import ItemCreate, ItemInDB
from app.utils.database import get_db

router = APIRouter()

# Create (POST)
@router.post("/", response_model=ItemInDB)
async def create_item_handler(item: ItemCreate, db: Session = Depends(get_db)):
    return await create_item(db=db, item=item)

# Read (GET)
@router.get("/{item_id}", response_model=ItemInDB)
async def get_item_handler(item_id: int, db: Session = Depends(get_db)):
    return await get_item(db=db, item_id=item_id)