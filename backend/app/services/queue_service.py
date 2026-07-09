from sqlalchemy.orm import Session

from app.models.queue import Queue
from app.schemas.queue import QueueCreate, QueueUpdate


def _next_queue_number(db: Session) -> str:
    last = db.query(Queue).order_by(Queue.id.desc()).first()
    next_id = (last.id + 1) if last else 1
    return f"Q{next_id:03d}"


def get_all(db: Session) -> list[Queue]:
    return db.query(Queue).order_by(Queue.id).all()


def get_by_id(db: Session, queue_id: int) -> Queue | None:
    return db.query(Queue).filter(Queue.id == queue_id).first()


def create(db: Session, payload: QueueCreate) -> Queue:
    queue = Queue(number=_next_queue_number(db), **payload.model_dump())
    db.add(queue)
    db.commit()
    db.refresh(queue)
    return queue


def update(db: Session, queue_id: int, payload: QueueUpdate) -> Queue | None:
    queue = get_by_id(db, queue_id)
    if not queue:
        return None

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(queue, field, value)

    db.commit()
    db.refresh(queue)
    return queue


def update_status(db: Session, queue_id: int, status: str) -> Queue | None:
    queue = get_by_id(db, queue_id)
    if not queue:
        return None

    queue.status = status
    db.commit()
    db.refresh(queue)
    return queue


def delete(db: Session, queue_id: int) -> bool:
    queue = get_by_id(db, queue_id)
    if not queue:
        return False

    db.delete(queue)
    db.commit()
    return True
