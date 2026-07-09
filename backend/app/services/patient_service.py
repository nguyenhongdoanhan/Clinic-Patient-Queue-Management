from sqlalchemy.orm import Session

from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientUpdate


def get_all(db: Session) -> list[Patient]:
    return db.query(Patient).order_by(Patient.id).all()


def get_by_id(db: Session, patient_id: int) -> Patient | None:
    return db.query(Patient).filter(Patient.id == patient_id).first()


def create(db: Session, payload: PatientCreate) -> Patient:
    patient = Patient(**payload.model_dump())
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient


def update(db: Session, patient_id: int, payload: PatientUpdate) -> Patient | None:
    patient = get_by_id(db, patient_id)
    if not patient:
        return None

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(patient, field, value)

    db.commit()
    db.refresh(patient)
    return patient


def delete(db: Session, patient_id: int) -> bool:
    patient = get_by_id(db, patient_id)
    if not patient:
        return False

    db.delete(patient)
    db.commit()
    return True
