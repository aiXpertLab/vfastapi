from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
# from app.api.r_report import reportRou

from app.api.r_wage_table import wageRou
from app.api.r_langchain import lcRou
from app.api.r_embedding import router as embeddingRou

rou = APIRouter()

@rou.get("/")
def rouGet():
    return RedirectResponse(url="https://ainvoaice.com")


rou.include_router(wageRou, prefix="/wages", tags=["Wages"])
# rou.include_router(agentRou, prefix="/agents", tags=["Agents"])
rou.include_router(embeddingRou, prefix="/embeddings", tags=["Embeddings"])
