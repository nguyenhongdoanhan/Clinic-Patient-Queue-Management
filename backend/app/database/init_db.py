from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.database.database import Base, SessionLocal, engine
from app.models import appointment, doctor, patient, queue, user  # noqa: F401 (đăng ký model với Base)
from app.models.user import User


def init_db() -> None:
    """Tạo toàn bộ bảng trong DB (nếu chưa có) và seed tài khoản Admin mặc định."""
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()
    try:
        _seed_admin(db)
    finally:
        db.close()


def _seed_admin(db: Session) -> None:
    admin_email = "admin@gmail.com"
    existing = db.query(User).filter(User.email == admin_email).first()
    if existing:
        return

    admin = User(
        name="Quản trị viên",
        email=admin_email,
        password_hash=hash_password("admin123"),
        role="Admin",
        status="Hoạt động",
    )
    db.add(admin)
    db.commit()
