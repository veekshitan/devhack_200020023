from fastapi import APIRouter, Depends, Request
from utils.postgres_operations import session
router=APIRouter()