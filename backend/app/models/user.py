from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class User(Base):
    """
    Tài khoản người dùng hệ thống.
    role: "Admin" | "Bác sĩ" | "Lễ tân" | "Bệnh nhân"
    status: "Hoạt động" | "Khóa"
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(30), default="Bệnh nhân", nullable=False)
    status: Mapped[str] = mapped_column(String(30), default="Hoạt động", nullable=False)
    phone: Mapped[str | None] = mapped_column(String(30), nullable=True)
    address: Mapped[str | None] = mapped_column(String(255), nullable=True)
