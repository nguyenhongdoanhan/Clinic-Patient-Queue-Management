from pydantic import BaseModel, ConfigDict


class AppointmentBase(BaseModel):
    patient: str
    doctor: str
    date: str
    time: str
    status: str = "Đã đặt"


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentUpdate(BaseModel):
    patient: str | None = None
    doctor: str | None = None
    date: str | None = None
    time: str | None = None
    status: str | None = None


class AppointmentOut(AppointmentBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
