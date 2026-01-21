from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
import uuid
from sqlalchemy.orm import Mapped, mapped_column
from app.db.models.m_base import Base, BaseMixin
from pgvector.sqlalchemy import Vector

class CanadaWageEmbedding(Base):
    __tablename__ = "wage_384"
    id: Mapped[uuid.UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid.uuid4,
    )

    source_id: Mapped[str] = mapped_column(PG_UUID(as_uuid=True), nullable=False)
    chunk_en: Mapped[str] = mapped_column(Text, nullable=False)
    chunk_fr: Mapped[str] = mapped_column(Text, nullable=False)
    bak: Mapped[str] = mapped_column(Text, nullable=True)   
    # raw SQL type for pgvector
    embedding: Mapped[list[float]] = mapped_column(
        Vector(384), nullable=False
    )