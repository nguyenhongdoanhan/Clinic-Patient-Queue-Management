from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: str = "Bệnh nhân"
    status: str = "Hoạt động"
    phone: str | None = None
    address: str | None = None


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    role: str | None = None
    status: str | None = None
    phone: str | None = None
    address: str | None = None


class UserOut(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str
