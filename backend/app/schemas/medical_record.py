from pydantic import BaseModel
from datetime import datetime


class MedicalRecordBase(BaseModel):
    patient_id: int
    doctor_id: int
    diagnosis: str | None = None
    treatment: str | None = None
    notes: str | None = None


class MedicalRecordCreate(MedicalRecordBase):
    pass


class MedicalRecordResponse(MedicalRecordBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
