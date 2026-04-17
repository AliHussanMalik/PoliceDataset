$ErrorActionPreference = "Stop"
$env:PYTHONPATH = "$(Resolve-Path .\src)"

Write-Host "Loading CSV into SQLite database..."
.\.venv\Scripts\python.exe -m police_dataset.ingest
