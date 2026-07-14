@echo off
echo Starting backend using backend\venv
if not exist backend\venv\Scripts\python.exe (
  echo backend\venv not found. Create it using system Python.
  exit /b 1
)
backend\venv\Scripts\python.exe backend\run.py