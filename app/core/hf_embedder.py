# app/integrations/hf_embedder.py
import httpx
from typing import List
from app.config import get_settings_singleton
settings = get_settings_singleton()

HF_URL = ("https://api-inference.huggingface.co/models/"+ settings.HF_EMBED_MODEL)

async def embed_fn(text: str) -> List[float]:
    headers = {
        "Authorization": f"Bearer {settings.HF_API_KEY}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(
            HF_URL,
            headers=headers,
            json={
                "inputs": text,
                "options": {"wait_for_model": True},
            },
        )
        r.raise_for_status()
        data = r.json()

        # token embeddings → mean pooled vector(384)
        return [sum(col) / len(col) for col in zip(*data)]
