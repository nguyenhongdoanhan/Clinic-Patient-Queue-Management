from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Patient(Base):
    """gender: "Nam" | "Nữ" """

    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    gender: Mapped[str] = mapped_column(String(10), default="Nam", nullable=False)
    birthday: Mapped[str | None] = mapped_column(String(20), nullable=True)
    phone: Mapped[str] = mapped_column(String(30), nullable=False)
    address: Mapped[str | None] = mapped_column(String(255), nullable=True)
