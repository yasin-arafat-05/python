from fastapi import APIRouter

router = APIRouter()

@router.get(path="/courses")
async def courses():
    return f"This is Courses Section."