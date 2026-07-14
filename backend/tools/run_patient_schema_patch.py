"""
Small helper to run the patient schema patch at any time.
Runs the existing `ensure_patient_schema` function from app.core.database.
"""
from app.core.database import ensure_patient_schema


def main():
    ensure_patient_schema()
    print("Patient schema patch attempted (see server logs for details).")


if __name__ == "__main__":
    main()
