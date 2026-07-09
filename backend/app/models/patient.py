<<<<<<< HEAD
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
=======
from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100))
    phone = Column(String(20))
    email = Column(String(100))
>>>>>>> aa42b3e (Complete Patient CRUD)
