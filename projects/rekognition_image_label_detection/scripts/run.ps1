Set-Location -LiteralPath $PSScriptRoot\..\src
if (-not (Test-Path -Path '.venv')) {
    python -m venv .venv
}
.\.venv\Scripts\Activate.ps1
python main.py
