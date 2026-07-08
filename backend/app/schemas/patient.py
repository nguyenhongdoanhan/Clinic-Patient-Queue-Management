from pydantic import BaseModel

class PatientCreate(BaseModel):
    full_name: str
    phone: str
    email: str


class PatientResponse(PatientCreate):
    id: int

    class Config:
        from_attributes = True