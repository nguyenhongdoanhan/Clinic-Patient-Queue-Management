from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date
from sqlalchemy import DateTime

from datetime import datetime

from app.core.database import Base


class Patient(Base):

    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(150), nullable=False)

    gender = Column(String(20))

    birthday = Column(Date)

    phone = Column(String(20))

    address = Column(String(255))

    created_at = Column(DateTime, default=datetime.utcnow)