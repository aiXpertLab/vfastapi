# app/api/routes/wage.py
from fastapi import APIRouter, Depends, UploadFile, File, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db_async import get_db
from app.service.ser_wage import WageService
from app.db.repo.repo_wage_embedding import WageEmbeddingRepository
from app.service.ser_wage_embedding import WageEmbeddingService
from app.core.openai_embedder import embed_fn


lcRou = APIRouter()

@lcRou.post("/agent1.1", summary="Wage Agent 1.1")
async def agent11():
    agent = await WageEmbeddingRepository.build_chunks()
    return {"count": len(chunks), "sample": chunks[:3]}
