from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime

from datetime import datetime

from app.core.database import Base


class MedicalRecord(Base):

    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True)

    patient_id = Column(Integer, ForeignKey("patients.id"))

    doctor_id = Column(Integer, ForeignKey("doctors.id"))

    diagnosis = Column(String(255))

    treatment = Column(Text)

    notes = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)
