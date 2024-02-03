from fastapi import APIRouter, Depends, Request
from utils.postgres_operations import session
from models.coupons_model import CouponsModel
from models.buy_coupons_model import BuyCouponsModel
from utils.coupons_utils import save_coupon, save_buy_coupon, delete_coupon
router=APIRouter()

@router.post("/coupons")
async def add_coupon_endpoint(request: CouponsModel):
    return save_coupon(request.roll_no, request.category)

@router.post("/buyCoupons")
async def buy_coupons_endpoint(request: BuyCouponsModel):
    return save_buy_coupon(request.roll_no,request.category)

@router.delete("/coupons")
async def del_coupon(request: CouponsModel):
    return delete_coupon(request.roll_no, request.category)