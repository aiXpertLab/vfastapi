from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import (String, Integer, Float, Date, Text, Boolean, Index,)
from app.db.models.m_base import Base, BaseMixin


class CanadaWage(Base, BaseMixin):
    __tablename__ = "wages"

    __table_args__ = (
        Index("idx_wages_noc_cnp", "noc_cnp"),
        Index("idx_wages_prov", "prov"),
        Index("idx_wages_er_code_code_re", "er_code_code_re"),
        Index("idx_wages_reference_period", "reference_period"),
        Index("idx_wages_noc_prov", "noc_cnp", "prov"),
    )

    # ---- Occupation ----
    noc_cnp: Mapped[str] = mapped_column(String(10), nullable=True)
    noc_title_eng: Mapped[str] = mapped_column(String(255), nullable=True)
    noc_title_fra: Mapped[str] = mapped_column(String(255), nullable=True)

    # ---- Geography ----
    prov: Mapped[str] = mapped_column(String(10), nullable=True)
    er_code_code_re: Mapped[str] = mapped_column(String(20), nullable=True)
    er_name: Mapped[str] = mapped_column(String(255), nullable=True)
    nom_re: Mapped[str] = mapped_column(String(255), nullable=True)

    # ---- Wages ----
    low_wage_salaire_minium: Mapped[int] = mapped_column(
        Integer, nullable=True)
    median_wage_salaire_median: Mapped[int] = mapped_column(
        Integer, nullable=True)
    high_wage_salaire_maximal: Mapped[int] = mapped_column(
        Integer, nullable=True)
    average_wage_salaire_moyen: Mapped[int] = mapped_column(
        Integer, nullable=True)
    quartile1_wage_salaire_quartile1: Mapped[int] = mapped_column(
        Integer, nullable=True)
    quartile3_wage_salaire_quartile3: Mapped[int] = mapped_column(
        Integer, nullable=True)

    # ---- Flags ----
    annual_wage_flag_salaire_annuel: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    # ---- Metadata ----
    source2025_nhq: Mapped[str] = mapped_column(String(255), nullable=True)
    data_source_e: Mapped[str] = mapped_column(String(255), nullable=True)
    data_source_f: Mapped[str] = mapped_column(String(255), nullable=True)

    reference_period: Mapped[str] = mapped_column(String(20), nullable=True)
    revision_date_date_revision: Mapped[Date] = mapped_column(
        Date, nullable=True)

    # ---- Notes ----
    wage_comment_e: Mapped[str] = mapped_column(Text, nullable=True)
    wage_comment_f: Mapped[str] = mapped_column(Text, nullable=True)

    # ---- Benefits ----
    employeeswithnonwagebenefit_pct: Mapped[float] = mapped_column(
        Float, nullable=True)
