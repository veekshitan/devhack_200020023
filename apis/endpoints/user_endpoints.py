from fastapi import APIRouter, Depends, Request
from utils.postgres_operations import session
from models.user_login_model import UserLoginModel
from utils.user_login import user_verification
router=APIRouter()

@router.post("/login")
async def user_login(request: UserLoginModel):
    return user_verification(request.roll_number, request.password)