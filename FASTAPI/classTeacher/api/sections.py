from fastapi import APIRouter

router = APIRouter()

@router.get('/sections')
async def sections():
    return f"This is Section Section."