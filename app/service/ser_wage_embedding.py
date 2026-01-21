# app/service/ser_wage.py
from typing import List, Dict
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.repo.repo_wage_embedding import WageEmbeddingRepository

class WageService:
    @staticmethod
    async def build_and_store_embeddings(
        db: AsyncSession,
        embed_fn,  # callable(text) -> list[float]
    ) -> int:
        chunks = await WageEmbeddingRepository.build_chunks(db)

        embeddings: List[Dict] = []
        for c in chunks:
            emb = embed_fn(c["chunk_en"])  # or combine EN+FR if you want
            embeddings.append(
                {
                    "source_id": c["source_id"],
                    "chunk_en": c["chunk_en"],
                    "chunk_fr": c["chunk_fr"],
                    "embedding": emb,
                }
            )

        await WageEmbeddingRepository.bulk_insert_embeddings(db, embeddings)
        return len(embeddings)
