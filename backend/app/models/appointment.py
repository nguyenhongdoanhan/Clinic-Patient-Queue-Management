from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Date
from sqlalchemy import Time
from sqlalchemy import ForeignKey

from app.core.database import Base


class Appointment(Base):

    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)

    patient_id = Column(Integer, ForeignKey("patients.id"))

    doctor_id = Column(Integer, ForeignKey("doctors.id"))

    appointment_date = Column(Date)

    appointment_time = Column(Time)