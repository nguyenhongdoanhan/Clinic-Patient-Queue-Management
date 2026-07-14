# Backend startup

This project uses a dedicated virtual environment at `backend\venv` for the API server.

Preferred startup (PowerShell):

```powershell
backend\venv\Scripts\python.exe backend\run.py
```

Or using the repo helper:

```powershell
.\start_backend.ps1
```

If `backend\venv` does not exist or is corrupted, recreate it using a system Python (64-bit recommended). Example commands:

```powershell
python -m venv backend\venv
backend\venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel
backend\venv\Scripts\python.exe -m pip install -r backend\requirements.txt
```

Notes:
- If some DB drivers (e.g. `pymssql`, `pyodbc`) or `cryptography` fail to build, you can still run the API using SQLite (`backend\clinic.db`) and add drivers later.
