<<<<<<< HEAD
from fastapi import APIRouter
from fastapi import Depends
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

    return db.query(Patient).filter(
        Patient.id == id
    ).first()


@router.post("")
def create(
        data: PatientCreate,
        db: Session = Depends(get_db)
):

    patient = Patient(**data.model_dump())

    db.add(patient)

    db.commit()

    db.refresh(patient)

    return patient


@router.put("/{id}")
def update(
        id: int,
        data: PatientCreate,
        db: Session = Depends(get_db)
):

    patient = db.query(Patient).filter(
        Patient.id == id
    ).first()

    if patient is None:

        return {"message": "Not found"}

    for key, value in data.model_dump().items():

        setattr(patient, key, value)

    db.commit()

    db.refresh(patient)

    return patient


@router.delete("/{id}")
def delete(
        id: int,
        db: Session = Depends(get_db)
):

    patient = db.query(Patient).filter(
        Patient.id == id
    ).first()

    if patient is None:

        return {"message": "Not found"}

    db.delete(patient)

    db.commit()

    return {"message": "Deleted"}
=======
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
>>>>>>> aa42b3e (Complete Patient CRUD)
