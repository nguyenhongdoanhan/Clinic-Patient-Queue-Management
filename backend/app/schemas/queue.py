from pydantic import BaseModel, ConfigDict


class QueueBase(BaseModel):
    patient: str
    doctor: str
    room: str
    status: str = "Đang chờ"


class QueueCreate(QueueBase):
    pass


class QueueUpdate(BaseModel):
    patient: str | None = None
    doctor: str | None = None
    room: str | None = None
    status: str | None = None


class QueueStatusUpdate(BaseModel):
    status: str


class QueueOut(QueueBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    number: str
