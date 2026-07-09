from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Doctor(Base):
    """status: "Đang làm việc" | "Nghỉ" """

    __tablename__ = "doctors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    specialty: Mapped[str] = mapped_column(String(150), nullable=False)
    phone: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    status: Mapped[str] = mapped_column(String(30), default="Đang làm việc", nullable=False)
