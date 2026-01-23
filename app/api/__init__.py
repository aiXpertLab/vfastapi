import httpx, markdown

from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
# from app.api.r_report import reportRou

from app.api.r_wage_table import wageRou
from app.api.r_langchain import lcRou
from app.api.r_embedding import router as embeddingRou

rou = APIRouter()
README_URL = "https://raw.githubusercontent.com/aiXpertLab/aiXpertLab/refs/heads/master/README.md"

# @rou.get("/")
# def rouGet():
#     return {"queries": "Welcome to Wildfire!",}

@rou.get("/")
async def rouGet():
    async with httpx.AsyncClient() as client:
        r = await client.get(README_URL)

    return HTMLResponse(markdown.markdown(r.text))

rou.include_router(wageRou, prefix="/wages", tags=["Wages"])
# rou.include_router(agentRou, prefix="/agents", tags=["Agents"])
rou.include_router(embeddingRou, prefix="/embeddings", tags=["Embeddings"])
