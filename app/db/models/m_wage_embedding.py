from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.models.m_base import Base, BaseMixin

class CanadaWageEmbedding(Base, BaseMixin):
    __tablename__ = "wage_384"

    source_id: Mapped[str] = mapped_column(UUID(as_uuid=True), nullable=False)
    chunk_en: Mapped[str] = mapped_column(Text, nullable=False)
    chunk_fr: Mapped[str] = mapped_column(Text, nullable=False)
    bak: Mapped[str] = mapped_column(Text, nullable=True)   
    # raw SQL type for pgvector
    embedding = mapped_column("embedding", nullable=False)
