from pydantic import BaseModel
from datetime import date


class PatientCreate(BaseModel):

    full_name: str

    gender: str

    birthday: date

    phone: str

    address: str


class PatientResponse(PatientCreate):

    id: int

    class Config:

        from_attributes = True