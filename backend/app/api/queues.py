from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.database.database import get_db
from app.schemas.queue import QueueCreate, QueueOut, QueueStatusUpdate, QueueUpdate
from app.services import queue_service

router = APIRouter(prefix="/queues", tags=["queues"], dependencies=[Depends(get_current_user)])


@router.get("", response_model=list[QueueOut])
def list_queues(db: Session = Depends(get_db)):
    return queue_service.get_all(db)


@router.post("", response_model=QueueOut, status_code=status.HTTP_201_CREATED)
def create_queue(payload: QueueCreate, db: Session = Depends(get_db)):
    return queue_service.create(db, payload)


@router.put("/{queue_id}", response_model=QueueOut)
def update_queue(queue_id: int, payload: QueueUpdate, db: Session = Depends(get_db)):
    queue = queue_service.update(db, queue_id, payload)
    if not queue:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy hàng đợi.")
    return queue


@router.patch("/{queue_id}/status", response_model=QueueOut)
def update_queue_status(queue_id: int, payload: QueueStatusUpdate, db: Session = Depends(get_db)):
    queue = queue_service.update_status(db, queue_id, payload.status)
    if not queue:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy hàng đợi.")
    return queue


@router.delete("/{queue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_queue(queue_id: int, db: Session = Depends(get_db)):
    deleted = queue_service.delete(db, queue_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Không tìm thấy hàng đợi.")
