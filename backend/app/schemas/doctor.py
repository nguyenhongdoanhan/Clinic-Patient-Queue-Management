from pydantic import BaseModel, ConfigDict


class DoctorBase(BaseModel):
    name: str
    specialty: str
    phone: str
    email: str
    status: str = "Đang làm việc"


class DoctorCreate(DoctorBase):
    pass


class DoctorUpdate(BaseModel):
    name: str | None = None
    specialty: str | None = None
    phone: str | None = None
    email: str | None = None
    status: str | None = None


class DoctorOut(DoctorBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
