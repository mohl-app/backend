from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..db import get_session
from ..models import Item

router = APIRouter()

@router.get("/healthz")
async def healthz(): return {"ok": True}

@router.get("/items")
async def list_items(db: AsyncSession = Depends(get_session)):
    rows = (await db.execute(select(Item))).scalars().all()
    return [{"id": i.id, "name": i.name} for i in rows]
