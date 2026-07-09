from sqlalchemy.orm import Session

from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate, AppointmentUpdate


def get_all(db: Session) -> list[Appointment]:
    return db.query(Appointment).order_by(Appointment.id).all()


def get_by_id(db: Session, appointment_id: int) -> Appointment | None:
    return db.query(Appointment).filter(Appointment.id == appointment_id).first()


def create(db: Session, payload: AppointmentCreate) -> Appointment:
    appointment = Appointment(**payload.model_dump())
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment


def update(db: Session, appointment_id: int, payload: AppointmentUpdate) -> Appointment | None:
    appointment = get_by_id(db, appointment_id)
    if not appointment:
        return None

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(appointment, field, value)

    db.commit()
    db.refresh(appointment)
    return appointment


def delete(db: Session, appointment_id: int) -> bool:
    appointment = get_by_id(db, appointment_id)
    if not appointment:
        return False

    db.delete(appointment)
    db.commit()
    return True
