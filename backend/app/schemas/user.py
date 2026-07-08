from pydantic import BaseModel
from pydantic import EmailStr


class Login(BaseModel):

    email: EmailStr

    password: str


class Register(BaseModel):

    username: str

    email: EmailStr

    password: str


class UserResponse(BaseModel):

    id: int

    username: str

    email: str

    role: str

    class Config:
        from_attributes = True