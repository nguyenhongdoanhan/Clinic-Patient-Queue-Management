from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Appointment(Base):
    """status: "Đã đặt" | "Đã khám" | "Đã hủy" """

    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    patient: Mapped[str] = mapped_column(String(150), nullable=False)
    doctor: Mapped[str] = mapped_column(String(150), nullable=False)
    date: Mapped[str] = mapped_column(String(20), nullable=False)
    time: Mapped[str] = mapped_column(String(10), nullable=False)
    status: Mapped[str] = mapped_column(String(30), default="Đã đặt", nullable=False)
