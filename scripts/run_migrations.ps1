$ErrorActionPreference = "Stop"
$env:PYTHONPATH = "$(Resolve-Path .\src)"

Write-Host "Running Alembic migrations..."
.\.venv\Scripts\python.exe -m alembic upgrade head
