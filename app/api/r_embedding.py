# app/api/routes/wage.py
from fastapi import APIRouter, Depends, UploadFile, File, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db_async import get_db
from app.service.ser_wage import WageService
from app.db.repo.repo_wage_embedding import WageEmbeddingRepository

router = APIRouter()

@router.post("/build-wage-chunks")
async def build_wage_chunks(db: AsyncSession = Depends(get_db)):
    chunks = await WageEmbeddingRepository.build_chunks(db)
    return {"count": len(chunks), "sample": chunks[:3]}