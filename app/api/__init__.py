from fastapi import APIRouter, Depends

# from app.api.r_report import reportRou
from app.api.r_wage_table import wageRou
from app.api.r_agent import agentRou
from app.api.r_embedding import router as embeddingRou

rou = APIRouter()

@rou.get("/")
def rouGet():
    return {"queries": "Welcome to Wildfire!",}



rou.include_router(wageRou, prefix="/wages", tags=["Wages"])
rou.include_router(agentRou, prefix="/agents", tags=["Agents"])
rou.include_router(embeddingRou, prefix="/embeddings", tags=["Embeddings"])
