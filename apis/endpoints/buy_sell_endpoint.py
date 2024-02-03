from fastapi import APIRouter, Depends, Request
from utils.buy_item import send_email_to_seller
from utils.postgres_operations import getSellerEmailID
from models.buy_model import UserBuyModel
from models.sell_model import SellModel
from models.delete_item_model import DeleteItemModel
from models.get_items_model import ItemsModel
from utils.sell_item import saveSaleItem, delete_item
from utils.get_item import get_all_items_in_category

router=APIRouter()

@router.post("/getItems")
async def getItemByCategory(request: ItemsModel):
    return get_all_items_in_category(request.category)

@router.post("/buyitem")
async def buyItem(request: UserBuyModel):
    item_name, seller_emailId, seller_name = getSellerEmailID(request.good_number)
    send_email_to_seller(request.roll_number, item_name, seller_name, seller_emailId)
    return seller_name
    
@router.post("/sellitem")
async def sellItem(request: SellModel):
   return saveSaleItem(request.roll_number, request.category, request.item_name, request.cost, request.images, request.unique_good_number)
    
@router.delete("/sellitem")
async def del_item(request: DeleteItemModel):
    return delete_item(request.good_number)
    