from fastapi import FastAPI

from app.database.database import Base, engine
from app.api.patient import router as patient_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(patient_router)


@app.get("/")
def read_root():
    return {"message": "Clinic API is running"}