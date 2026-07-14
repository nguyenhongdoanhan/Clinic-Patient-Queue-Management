import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Load the backend/.env file regardless of the current working directory.
dotenv_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path)

# Read DATABASE_URL from environment and require MySQL.
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError(
        "DATABASE_URL is not set. Set DATABASE_URL in backend/.env to your MySQL connection string."
    )

if not DATABASE_URL.startswith(("mysql://", "mysql+pymysql://")):
    raise RuntimeError(
        "DATABASE_URL must be a MySQL connection string, for example: mysql+pymysql://user:pass@host:3306/dbname"
    )

# MySQL backend only.
connect_args = {}

# Try to create the engine for the configured DATABASE_URL.
# If the configured remote DB fails, raise immediately so the issue is visible.
try:
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
        connect_args=connect_args,
    )
    # Test a connection immediately to surface configuration errors early
    with engine.connect() as conn:  # type: ignore
        pass
except SQLAlchemyError as e:
    print("⚠️  Failed to connect using DATABASE_URL:", DATABASE_URL)
    print("Error:", str(e))
    raise


def ensure_patient_schema():
    """Fix missing patient table columns on old database schema."""
    try:
        inspector = inspect(engine)
        if "patients" not in inspector.get_table_names():
            return

        columns = [column["name"] for column in inspector.get_columns("patients")]
        statements = []

        if "gender" not in columns:
            statements.append("ALTER TABLE patients ADD COLUMN gender VARCHAR(20) NULL")
        if "birthday" not in columns:
            statements.append("ALTER TABLE patients ADD COLUMN birthday DATE NULL")
        if "phone" not in columns:
            statements.append("ALTER TABLE patients ADD COLUMN phone VARCHAR(20) NULL")
        if "email" not in columns:
            statements.append("ALTER TABLE patients ADD COLUMN email VARCHAR(100) NULL")
        if "address" not in columns:
            statements.append("ALTER TABLE patients ADD COLUMN address VARCHAR(255) NULL")
        if "created_at" not in columns:
            statements.append("ALTER TABLE patients ADD COLUMN created_at DATETIME NULL")

        if not statements:
            return

        with engine.connect() as conn:
            for statement in statements:
                conn.execute(text(statement))
            conn.commit()
            print("✅ Applied patient schema patch: added missing columns.")
    except SQLAlchemyError as e:
        print("⚠️  Could not patch patient schema:", e)

# Session factory and declarative base
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()