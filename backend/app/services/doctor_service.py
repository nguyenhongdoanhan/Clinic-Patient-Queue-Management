from sqlalchemy.orm import Session

from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate


def get_all(db: Session) -> list[Doctor]:
    return db.query(Doctor).order_by(Doctor.id).all()


def get_by_id(db: Session, doctor_id: int) -> Doctor | None:
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()


def create(db: Session, payload: DoctorCreate) -> Doctor:
    doctor = Doctor(**payload.model_dump())
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor


def update(db: Session, doctor_id: int, payload: DoctorUpdate) -> Doctor | None:
    doctor = get_by_id(db, doctor_id)
    if not doctor:
        return None

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(doctor, field, value)

    db.commit()
    db.refresh(doctor)
    return doctor


def delete(db: Session, doctor_id: int) -> bool:
    doctor = get_by_id(db, doctor_id)
    if not doctor:
        return False

    db.delete(doctor)
    db.commit()
    return True
