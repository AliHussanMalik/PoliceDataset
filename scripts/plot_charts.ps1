$ErrorActionPreference = "Stop"
$env:PYTHONPATH = "$(Resolve-Path .\src)"

Write-Host "Generating PNG visualizations..."
.\.venv\Scripts\python.exe -m police_dataset.visualization
