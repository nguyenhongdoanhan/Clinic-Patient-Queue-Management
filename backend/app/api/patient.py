from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.patient import PatientCreate
from app.services.patient_service import (
    get_all_patients,
    create_patient,
    get_patient_by_id
)

router = APIRouter(
    prefix="/patient",
    tags=["Patient"]
)


@router.get("/")
def get_patients(db: Session = Depends(get_db)):
    return get_all_patients(db)


@router.post("/")
def add_patient(patient: PatientCreate,
                db: Session = Depends(get_db)):
    return create_patient(db, patient)
@router.get("/{patient_id}")
def get_patient(patient_id: int,
                db: Session = Depends(get_db)):

    patient = get_patient_by_id(db, patient_id)

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient