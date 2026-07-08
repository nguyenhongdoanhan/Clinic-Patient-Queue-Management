from sqlalchemy.orm import Session

from app.models.patient import Patient
from app.schemas.patient import PatientCreate


def get_all_patients(db: Session):
    return db.query(Patient).all()


def create_patient(db: Session, patient: PatientCreate):
    new_patient = Patient(
        full_name=patient.full_name,
        phone=patient.phone,
        email=patient.email
    )
    

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient
def get_patient_by_id(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()