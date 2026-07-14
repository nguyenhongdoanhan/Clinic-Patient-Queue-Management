from datetime import date
from typing import Optional
from pydantic import BaseModel


class PatientCreate(BaseModel):
    full_name: str
    gender: Optional[str] = None
    birthday: Optional[date] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None


class PatientResponse(PatientCreate):
    id: int

    class Config:
        from_attributes = True