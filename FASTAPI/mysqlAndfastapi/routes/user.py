from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from config.db import db_get
from schemas.user import Users
from models.user import User
from typing import Annotated
db_dependency = [Session,Depends(db_get)]
router = APIRouter()

@router.get('/getAllUser')
def fetch_users(db:db_dependency):
    user = db.
    return user