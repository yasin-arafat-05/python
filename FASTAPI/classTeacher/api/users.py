from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
async def users():
    return "This is User Section."
