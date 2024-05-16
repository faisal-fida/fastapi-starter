from fastapi import APIRouter
from app.services.item_service import send_email_by_sendgrid

router = APIRouter()


# Read (GET)
@router.get("/send_email")
async def send():
    return await send_email_by_sendgrid()
