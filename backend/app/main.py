from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine, SessionLocal
from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.patients import router as patients_router
from app.api.doctor import router as doctor_router
from app.api.appointments import router as appointments_router
from app.api.queues import router as queues_router
from app.api.medical_records import router as medical_records_router
from app.models.user import User
from app.core.security import hash_password

app = FastAPI(
    title="Clinic API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(patients_router)
app.include_router(doctor_router)
app.include_router(appointments_router)
app.include_router(queues_router)
app.include_router(medical_records_router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    
    # Create default admin user
    db = SessionLocal()
    try:
        # Check if admin user exists
        admin = db.query(User).filter(User.email == "admin@clinic.com").first()
        if not admin:
            admin_user = User(
                username="admin",
                email="admin@clinic.com",
                password=hash_password("admin123"),
                role="ADMIN"
            )
            db.add(admin_user)
            db.commit()
            print("✅ Default admin user created: admin@clinic.com / admin123")
    finally:
        db.close()


@app.get("/")
def home():
    return {
        "message": "Clinic API Running"
    }