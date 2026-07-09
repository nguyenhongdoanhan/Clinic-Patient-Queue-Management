from sqlalchemy.orm import Session

from app.core.security import create_access_token, hash_password, verify_password
from app.models.user import User
from app.schemas.user import UserCreate


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def register_user(db: Session, payload: UserCreate) -> User:
    existing = get_user_by_email(db, payload.email)
    if existing:
        raise ValueError("Email đã được sử dụng.")

    user = User(
        name=payload.name,
        email=payload.email,
        password_hash=hash_password(payload.password),
        role=payload.role or "Bệnh nhân",
        status=payload.status or "Hoạt động",
        phone=payload.phone,
        address=payload.address,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, email: str, password: str) -> User | None:
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.password_hash):
        return None
    if user.status == "Khóa":
        raise PermissionError("Tài khoản đã bị khóa.")
    return user


def create_user_token(user: User) -> str:
    return create_access_token({"sub": str(user.id), "email": user.email, "role": user.role})


def change_password(db: Session, user: User, old_password: str, new_password: str) -> User:
    if not verify_password(old_password, user.password_hash):
        raise ValueError("Mật khẩu cũ không đúng.")

    user.password_hash = hash_password(new_password)
    db.commit()
    db.refresh(user)
    return user
