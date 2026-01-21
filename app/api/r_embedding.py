# app/api/routes/wage.py
from fastapi import APIRouter, Depends, UploadFile, File, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db_async import get_db
from app.service.ser_wage import WageService
from app.db.repo.repo_wage_embedding import WageEmbeddingRepository
from app.service.ser_wage_embedding import WageService

router = APIRouter()

@router.post("/build-wage-chunks")
async def build_wage_chunks(db: AsyncSession = Depends(get_db)):
    chunks = await WageEmbeddingRepository.build_chunks(db)
    return {"count": len(chunks), "sample": chunks[:3]}


# app/api/routes/wage.py
@router.post("/build-wage-embeddings")
async def build_wage_embeddings(db: AsyncSession = Depends(get_db)):
    def dummy_embed(text: str) -> list[float]:
        return [0.0] * 384  # replace with OpenAI / local model

    count = await WageService.build_and_store_embeddings(db, dummy_embed)
    return {"inserted": count}
