from fastapi import APIRouter, Depends, Request
from utils.buy_item import send_email_to_seller
from utils.postgres_operations import getSellerEmailID
from models.buy_model import UserBuyModel
import json
from models.sell_model import SellModel
from models.delete_item_model import DeleteItemModel
from models.get_items_model import ItemsModel
from utils.sell_item import saveSaleItem, delete_item
from utils.get_item import get_all_items_in_category
from utils.coupons_utils import download_csv
router=APIRouter()

@router.post("/getItems")
async def getItemByCategory(request: ItemsModel):
    print(request.category, "this is the category we get")
    res = get_all_items_in_category(request.category)
    print(res, "this is thr ressssss")
    print([{**i.__dict__, **j.__dict__} for i,j in res])
    return [{**i.__dict__, **j.__dict__} for i,j in res]

@router.post("/buyitem")
async def buyItem(request: UserBuyModel):
    item_name, seller_emailId, seller_name = getSellerEmailID(request.good_number)
    send_email_to_seller(request.roll_number, item_name, seller_name, seller_emailId)
    return seller_name
    
@router.post("/sellitem")
async def sellItem(request: SellModel):
   return saveSaleItem(request.roll_number, request.category, request.item_name, request.cost, request.images)
    
@router.delete("/sellitem")
async def del_item(request: DeleteItemModel):
    return delete_item(request.good_number)
    
@router.post("/getCSV")
async def get_csv():
    res = (download_csv())
    print([i.__dict__ for i in res])
    return [i.__dict__ for i in res]