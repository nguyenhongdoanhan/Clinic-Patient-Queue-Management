from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.database.database import get_db
from app.models.user import User
from app.schemas.auth import LoginRequest, TokenResponse
from app.schemas.user import ChangePasswordRequest, UserCreate, UserOut
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    try:
        # Người dùng tự đăng ký luôn là "Bệnh nhân", không được tự chọn vai trò khác
        payload.role = "Bệnh nhân"
        payload.status = "Hoạt động"
        user = auth_service.register_user(db, payload)
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
    return user


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    try:
        user = auth_service.authenticate_user(db, payload.email, payload.password)
    except PermissionError as err:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(err))

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email hoặc mật khẩu không đúng.",
        )

    token = auth_service.create_user_token(user)
    return TokenResponse(access_token=token, user=user)


@router.get("/profile", response_model=UserOut)
def profile(current_user: User = Depends(get_current_user)):
    return current_user


@router.put("/change-password", response_model=UserOut)
def change_password(
    payload: ChangePasswordRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        user = auth_service.change_password(
            db, current_user, payload.old_password, payload.new_password
        )
    except ValueError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
    return user


@router.post("/logout")
def logout(current_user: User = Depends(get_current_user)):
    # JWT không lưu trạng thái ở server, việc "đăng xuất" thực hiện ở phía client
    # (xoá token). Endpoint này tồn tại để frontend có thể gọi khi cần.
    return {"message": "Đăng xuất thành công."}
