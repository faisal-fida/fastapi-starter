from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.item_model import Item
from app.schemas.item_schema import ItemCreate, ItemInDB

async def create_item(db: Session, item: ItemCreate):

    # Use this if you want to set a value differently or add a value
    """
    item_dict = item.model_dump() 
    item_dict['description'] = 'hi'
    new_item = Item(**item_dict) 
    """

    # Use this in case you want to use request obj as it is
    new_item = Item(**item.model_dump())
    db.add(new_item)
    db.commit()
    return ItemInDB(**new_item.dict())

async def get_item(db: Session, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return item