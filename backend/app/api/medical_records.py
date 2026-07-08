from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.medical_record import MedicalRecord
from app.schemas.medical_record import MedicalRecordCreate
from app.schemas.medical_record import MedicalRecordResponse

router = APIRouter(
    prefix="/api/medical_records",
    tags=["MedicalRecords"]
)


@router.get("", response_model=list[MedicalRecordResponse])
def get_all(db: Session = Depends(get_db)):
    return db.query(MedicalRecord).all()


@router.get("/{id}", response_model=MedicalRecordResponse)
def get_one(id: int, db: Session = Depends(get_db)):
    record = db.query(MedicalRecord).filter(MedicalRecord.id == id).first()
    if record is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medical record not found")
    return record


@router.post("", response_model=MedicalRecordResponse, status_code=status.HTTP_201_CREATED)
def create(data: MedicalRecordCreate, db: Session = Depends(get_db)):
    record = MedicalRecord(**data.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


@router.put("/{id}", response_model=MedicalRecordResponse)
def update(id: int, data: MedicalRecordCreate, db: Session = Depends(get_db)):
    record = db.query(MedicalRecord).filter(MedicalRecord.id == id).first()
    if record is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medical record not found")
    for key, value in data.model_dump().items():
        setattr(record, key, value)
    db.commit()
    db.refresh(record)
    return record


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    record = db.query(MedicalRecord).filter(MedicalRecord.id == id).first()
    if record is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Medical record not found")
    db.delete(record)
    db.commit()
    return {"message": "Deleted"}
