from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Queue(Base):
    """status: "Đang chờ" | "Đang khám" | "Đã hoàn thành" """

    __tablename__ = "queues"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    number: Mapped[str] = mapped_column(String(20), nullable=False)
    patient: Mapped[str] = mapped_column(String(150), nullable=False)
    doctor: Mapped[str] = mapped_column(String(150), nullable=False)
    room: Mapped[str] = mapped_column(String(30), nullable=False)
    status: Mapped[str] = mapped_column(String(30), default="Đang chờ", nullable=False)
