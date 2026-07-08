"""
Script to initialize SQL Server database for Clinic system
"""
import sqlalchemy as sa
from sqlalchemy import text
import os
from dotenv import load_dotenv

load_dotenv()

# Connection string without database
server_url = "mssql+pyodbc://sa:MyPassword@123@localhost:1433?driver=ODBC+Driver+17+for+SQL+Server"

def create_database():
    """Create clinic_db database if it doesn't exist"""
    try:
        # Connect to master database
        engine = sa.create_engine(server_url)
        
        with engine.connect() as conn:
            # Check if database exists
            result = conn.execute(text("SELECT name FROM sys.databases WHERE name = 'clinic_db'"))
            if result.fetchone() is None:
                # Create database
                conn.execute(text("CREATE DATABASE clinic_db"))
                conn.commit()
                print("✅ Database 'clinic_db' created successfully")
            else:
                print("✅ Database 'clinic_db' already exists")
                
        engine.dispose()
    except Exception as e:
        print(f"❌ Error creating database: {e}")

def create_tables():
    """Create all tables using SQLAlchemy models"""
    try:
        from app.core.database import engine, Base
        
        # Create all tables
        Base.metadata.create_all(bind=engine)
        print("✅ All tables created successfully")
        
    except Exception as e:
        print(f"❌ Error creating tables: {e}")

if __name__ == "__main__":
    print("🔧 Initializing SQL Server database...")
    create_database()
    create_tables()
    print("✅ Database initialization complete!")
