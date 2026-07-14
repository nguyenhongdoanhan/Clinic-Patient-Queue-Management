from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.patient import Patient
from app.schemas.patient import PatientCreate

router = APIRouter(
    prefix="/api/patients",
    tags=["Patients"]
)


@router.get("")
def get_all(db: Session = Depends(get_db)):
    return db.query(Patient).all()


@router.get("/{id}")
def get_one(id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id == id).first()

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


@router.post("")
def create(data: PatientCreate,
           db: Session = Depends(get_db)):
    patient = Patient(**data.model_dump())

    db.add(patient)
    db.commit()
    db.refresh(patient)

    return patient


@router.put("/{id}")
def update(id: int,
           data: PatientCreate,
           db: Session = Depends(get_db)):

    patient = db.query(Patient).filter(Patient.id == id).first()

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    for key, value in data.model_dump().items():
        setattr(patient, key, value)

    db.commit()
    db.refresh(patient)

    return patient


@router.delete("/{id}")
def delete(id: int,
           db: Session = Depends(get_db)):

    patient = db.query(Patient).filter(Patient.id == id).first()

    if patient is None:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    db.delete(patient)
    db.commit()

    return {"message": "Patient deleted successfully"}