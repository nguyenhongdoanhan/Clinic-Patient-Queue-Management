from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.core.database import Base


class Doctor(Base):

    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)

    full_name = Column(String(150), nullable=False)

    specialty = Column(String(100))

    phone = Column(String(20))

    email = Column(String(100))