from fastapi import APIRouter, Depends, Request
from utils.buy_item import send_email_to_seller
from utils.postgres_operations import getSellerEmailID
from models.buy_model import UserBuyModel
from models.sell_model import SellModel
from utils.sell_item import saveSaleItem

router=APIRouter()

@router.post("/buyitem")
async def buyItem(request: UserBuyModel):
    item_name, seller_emailId, seller_name = getSellerEmailID(request.good_number)
    return send_email_to_seller(request.roll_number, item_name, seller_name, seller_emailId)
    
@router.post("/sellitem")
async def sellItem(request: SellModel):
   return saveSaleItem(request.roll_number, request.category, request.item_name, request.cost, request.images, request.unique_good_number)
    