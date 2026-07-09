from pydantic import BaseModel
<<<<<<< HEAD
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

=======

class PatientCreate(BaseModel):
    full_name: str
    phone: str
    email: str


class PatientResponse(PatientCreate):
    id: int

    class Config:
>>>>>>> aa42b3e (Complete Patient CRUD)
        from_attributes = True