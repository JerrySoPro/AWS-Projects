# Rekognition — Image Label Detection

This project processes images stored in an S3 bucket and detects labels using Amazon Rekognition.

Quick start

1. Configure AWS credentials (aws configure or environment variables)
2. Create a virtualenv and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. Update the S3 bucket name in `src/main.py` or provide via environment variable `REKOGNITION_BUCKET`.

4. Run the script:

```powershell
Set-Location -LiteralPath "./projects/rekognition_image_label_detection/src"
python main.py
```

Files

- `src/main.py` — main script and helper functions
- `requirements.txt` — runtime dependencies
- `tests/` — small unit tests (uses mocking)

Notes

- Keep credentials and sensitive data out of the repo. Use IAM with least privilege.
- This project is intended as a single, focused mini-project inside a multi-project repo.
