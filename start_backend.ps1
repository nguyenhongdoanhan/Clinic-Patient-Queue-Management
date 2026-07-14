param(
    [string]$Port = "8080"
)

Write-Host "Starting backend using backend\venv..."
if (-Not (Test-Path "backend\venv\Scripts\python.exe")) {
    Write-Error "backend\venv\Scripts\python.exe not found. Create the venv first with system Python."
    exit 1
}

& backend\venv\Scripts\python.exe backend\run.py