"""Migrate `patients` table from local sqlite (backend/clinic.db) to a remote DB.

Usage:
  Set DEST_DATABASE_URL environment variable or pass --dest on CLI.
  Example MySQL URL: mysql+pymysql://user:pass@host:3306/dbname
  Example MSSQL URL (pyodbc): mssql+pyodbc://user:pass@host:1433/dbname?driver=ODBC+Driver+18+for+SQL+Server

Run:
  python migrate_sqlite_to_remote.py --source backend/clinic.db --dest "mysql+pymysql://..."

Notes:
  - Make sure remote DB is reachable and credentials are correct.
  - Install required drivers in your backend venv: `pip install pymysql` for MySQL, and `pip install pyodbc` plus the Microsoft ODBC driver for SQL Server if using MSSQL.
"""
import argparse
import os
import sqlite3
from datetime import datetime

from sqlalchemy import create_engine, Table, Column, Integer, String, Date, DateTime, MetaData


def ensure_dest_table(engine):
    meta = MetaData()
    patients = Table(
        "patients",
        meta,
        Column("id", Integer, primary_key=True),
        Column("full_name", String(150), nullable=False),
        Column("gender", String(20), nullable=True),
        Column("birthday", Date, nullable=True),
        Column("phone", String(20), nullable=True),
        Column("email", String(100), nullable=True),
        Column("address", String(255), nullable=True),
        Column("created_at", DateTime, nullable=True),
    )
    meta.create_all(engine)
    return patients


def copy_rows(source_path, dest_url):
    if not os.path.exists(source_path):
        raise SystemExit(f"Source sqlite file not found: {source_path}")

    dest_engine = create_engine(dest_url, pool_pre_ping=True)
    patients_table = ensure_dest_table(dest_engine)

    src = sqlite3.connect(source_path)
    src.row_factory = sqlite3.Row
    cur = src.cursor()
    cur.execute("SELECT id, full_name, gender, birthday, phone, email, address, created_at FROM patients ORDER BY id")

    rows = cur.fetchall()
    if not rows:
        print("No rows found in source patients table.")
        return

    inserted = 0
    with dest_engine.begin() as conn:
        for r in rows:
            # Convert sqlite row to dict and normalize types
            data = dict(r)
            # Parse birthday and created_at if present
            if data.get("birthday"):
                try:
                    # SQLite stores date as text YYYY-MM-DD or datetime
                    data["birthday"] = datetime.fromisoformat(data["birthday"]).date()
                except Exception:
                    try:
                        data["birthday"] = datetime.strptime(data["birthday"], "%Y-%m-%d").date()
                    except Exception:
                        data["birthday"] = None
            if data.get("created_at"):
                try:
                    data["created_at"] = datetime.fromisoformat(data["created_at"])
                except Exception:
                    try:
                        data["created_at"] = datetime.strptime(data["created_at"], "%Y-%m-%d %H:%M:%S")
                    except Exception:
                        data["created_at"] = None

            # Insert or replace by primary key
            insert_stmt = patients_table.insert().prefix_with("OR REPLACE") if dest_engine.dialect.name == "sqlite" else patients_table.insert()
            try:
                conn.execute(insert_stmt.values(**data))
                inserted += 1
            except Exception as e:
                print("Failed to insert row id", data.get("id"), "error:", e)

    print(f"Finished. Inserted/updated {inserted} rows into {dest_url}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source", default="backend/clinic.db", help="Path to source sqlite file")
    p.add_argument("--dest", default=os.environ.get("DEST_DATABASE_URL"), help="Destination SQLAlchemy URL")
    args = p.parse_args()

    if not args.dest:
        p.error("Destination database URL must be provided via --dest or DEST_DATABASE_URL env var")

    print("Source:", args.source)
    print("Destination:", args.dest)
    copy_rows(args.source, args.dest)


if __name__ == "__main__":
    main()
