from pydantic import BaseModel


class DoctorBase(BaseModel):
    full_name: str
    specialty: str | None = None
    phone: str | None = None
    email: str | None = None


class DoctorCreate(DoctorBase):
    pass


class DoctorResponse(DoctorBase):
    id: int

    class Config:
        from_attributes = True
