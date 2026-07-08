from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from app.core.database import Base


class Queue(Base):

    __tablename__ = "queues"

    id = Column(Integer, primary_key=True)

    queue_number = Column(String(20))

    patient_id = Column(Integer, ForeignKey("patients.id"))

    doctor_id = Column(Integer, ForeignKey("doctors.id"))

    status = Column(String(30), default="WAITING")