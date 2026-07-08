from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.queue import Queue
from app.schemas.queue import QueueCreate
from app.schemas.queue import QueueResponse

router = APIRouter(
    prefix="/api/queues",
    tags=["Queues"]
)


@router.get("", response_model=list[QueueResponse])
def get_all(db: Session = Depends(get_db)):
    return db.query(Queue).all()


@router.get("/{id}", response_model=QueueResponse)
def get_one(id: int, db: Session = Depends(get_db)):
    queue = db.query(Queue).filter(Queue.id == id).first()
    if queue is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Queue not found")
    return queue


@router.post("", response_model=QueueResponse, status_code=status.HTTP_201_CREATED)
def create(data: QueueCreate, db: Session = Depends(get_db)):
    queue = Queue(**data.model_dump())
    db.add(queue)
    db.commit()
    db.refresh(queue)
    return queue


@router.put("/{id}", response_model=QueueResponse)
def update(id: int, data: QueueCreate, db: Session = Depends(get_db)):
    queue = db.query(Queue).filter(Queue.id == id).first()
    if queue is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Queue not found")
    for key, value in data.model_dump().items():
        setattr(queue, key, value)
    db.commit()
    db.refresh(queue)
    return queue


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    queue = db.query(Queue).filter(Queue.id == id).first()
    if queue is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Queue not found")
    db.delete(queue)
    db.commit()
    return {"message": "Deleted"}
