from fastapi import APIRouter, Depends, Request
from utils.buy_item import send_email_to_seller
from utils.postgres_operations import getSellerEmailID
from models.buy_model import UserBuyModel

router=APIRouter()

@router.post("/buyitem")
async def buyItem(request: UserBuyModel):
    item_name, seller_emailId, seller_name = getSellerEmailID(request.good_number)
    return send_email_to_seller(request.roll_number, item_name, seller_name, seller_emailId)
    