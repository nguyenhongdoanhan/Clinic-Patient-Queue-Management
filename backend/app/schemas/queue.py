from pydantic import BaseModel


class QueueBase(BaseModel):
    queue_number: str
    patient_id: int
    doctor_id: int
    status: str = "WAITING"


class QueueCreate(QueueBase):
    pass


class QueueResponse(QueueBase):
    id: int

    class Config:
        from_attributes = True
