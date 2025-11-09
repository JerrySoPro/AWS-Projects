# AWS Rekognition Image Label Detection

## Overview

This project provides a Python script that automatically detects labels in images stored in an AWS S3 bucket using Amazon Rekognition. The script processes all images in a specified bucket, analyzes them using machine learning, and returns detected objects, scenes, activities, and concepts with confidence scores.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [AWS Setup](#aws-setup)
- [Configuration](#configuration)
- [Usage](#usage)
- [Output](#output)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Cost Considerations](#cost-considerations)
- [File Structure](#file-structure)

## Features

- Batch processing of all images in an S3 bucket
- Automatic detection of JPEG and PNG images
- Detailed label information including:
  - Label names with confidence scores
  - Bounding box coordinates for detected objects
  - Parent category relationships
- Error handling for invalid images
- Comprehensive summary report with success/failure statistics
- Configurable via environment variables
- Unit tests with mocking for AWS services

## Prerequisites

Before using this project, ensure you have:

- Python 3.7 or higher installed
- An AWS account with appropriate permissions
- AWS CLI installed and configured
- Basic understanding of AWS S3 and Rekognition services
- An S3 bucket with images to process

## Installation

### 1. Navigate to Project Directory

```powershell
Set-Location -LiteralPath "./projects/rekognition_image_label_detection"
```

### 2. Create Virtual Environment

```powershell
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
.venv\Scripts\activate.bat
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```powershell
pip install -r requirements.txt
```

The `requirements.txt` includes:

- `boto3>=1.26.0` - AWS SDK for Python
- `botocore>=1.29.0` - Low-level interface to AWS services

## AWS Setup

### Step 1: Create an S3 Bucket

#### Using AWS Console

1. Sign in to the AWS Management Console
2. Navigate to S3 service
3. Click "Create bucket"
4. Enter a unique bucket name (e.g., `my-rekognition-images`)
5. Select your preferred AWS Region (e.g., `us-east-1`)
6. Leave other settings as default or configure as needed
7. Click "Create bucket"

#### Using AWS CLI

```bash
aws s3 mb s3://my-rekognition-images --region us-east-1
```

### Step 2: Upload Images

#### Using AWS Console

1. Open your bucket in the S3 console
2. Click "Upload"
3. Add your JPEG or PNG images
4. Click "Upload"

#### Using AWS CLI

```bash
# Upload a single file
aws s3 cp image.jpg s3://my-rekognition-images/

# Upload multiple files from a directory
aws s3 cp ./images/ s3://my-rekognition-images/ --recursive --exclude "*" --include "*.jpg" --include "*.png"
```

### Step 3: Configure IAM Permissions

Create an IAM user or role with the following permissions:

**Required Policies:**

- `AmazonS3ReadOnlyAccess` - To read images from S3
- `AmazonRekognitionFullAccess` - To use Rekognition DetectLabels API

#### Create IAM User (AWS Console)

1. Navigate to IAM in AWS Console
2. Click "Users" > "Create user"
3. Enter username (e.g., `rekognition-app`)
4. Click "Next"
5. Select "Attach policies directly"
6. Search and select the required policies above
7. Click "Next" > "Create user"
8. Create access keys for the user:
   - Click on the user
   - Go to "Security credentials" tab
   - Click "Create access key"
   - Select "Command Line Interface (CLI)"
   - Download the credentials CSV file
   - Save the Access Key ID and Secret Access Key securely

### Step 4: Configure AWS Credentials

#### Option 1: AWS CLI Configuration

```bash
aws configure
```

Enter your credentials when prompted:

```
AWS Access Key ID: YOUR_ACCESS_KEY_ID
AWS Secret Access Key: YOUR_SECRET_ACCESS_KEY
Default region name: us-east-1
Default output format: json
```

#### Option 2: Environment Variables

**Windows PowerShell:**

```powershell
$env:AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY_ID"
$env:AWS_SECRET_ACCESS_KEY="YOUR_SECRET_ACCESS_KEY"
$env:AWS_DEFAULT_REGION="us-east-1"
```

**Linux/macOS:**

```bash
export AWS_ACCESS_KEY_ID="YOUR_ACCESS_KEY_ID"
export AWS_SECRET_ACCESS_KEY="YOUR_SECRET_ACCESS_KEY"
export AWS_DEFAULT_REGION="us-east-1"
```

#### Option 3: Credentials File

Create or edit `~/.aws/credentials`:

```ini
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```

Create or edit `~/.aws/config`:

```ini
[default]
region = us-east-1
output = json
```

## Configuration

The script can be configured using environment variables:

### Environment Variables

| Variable             | Description                       | Default Value            | Required |
| -------------------- | --------------------------------- | ------------------------ | -------- |
| `REKOGNITION_BUCKET` | S3 bucket name containing images  | `project-rekognition-s3` | No       |
| `AWS_REGION`         | AWS region for S3 and Rekognition | `us-east-1`              | No       |

### Setting Environment Variables

**Windows PowerShell:**

```powershell
$env:REKOGNITION_BUCKET="my-rekognition-images"
$env:AWS_REGION="us-west-2"
```

**Linux/macOS:**

```bash
export REKOGNITION_BUCKET="my-rekognition-images"
export AWS_REGION="us-west-2"
```

### Modifying Default Values

Alternatively, you can edit the default values directly in `src/main.py`:

```python
def main():
    bucket = os.environ.get('REKOGNITION_BUCKET', 'your-bucket-name')
    region = os.environ.get('AWS_REGION', 'your-preferred-region')
```

## Usage

### Running the Script

#### Method 1: Direct Execution

```powershell
# Navigate to the src directory
Set-Location -LiteralPath "./src"

# Run the script
python main.py
```

#### Method 2: Using Helper Script

```powershell
# Navigate to scripts directory
Set-Location -LiteralPath "./scripts"

# Run the helper script (creates venv if needed)
.\run.ps1
```

#### Method 3: As a Module

```powershell
# From the project root
python -m projects.rekognition_image_label_detection.src.main
```

### Script Workflow

The script performs the following operations:

1. Connects to the specified S3 bucket
2. Lists all objects and filters for JPEG and PNG images
3. For each image:
   - Calls AWS Rekognition DetectLabels API
   - Retrieves up to 5 labels per image (configurable)
   - Displays label information with confidence scores
   - Shows bounding boxes for detected object instances
   - Lists parent categories for each label
4. Generates a summary report with statistics

## Output

### Sample Output

```
Fetching images from bucket: my-rekognition-images
Found 3 image(s) in the bucket
Files: dog.jpg, city.png, beach.jpeg
============================================================

============================================================
Detected labels for dog.jpg

Label: Dog
Confidence: 99.87
Instances:
  Bounding box
    Top: 0.123
    Left: 0.234
    Width: 0.456
    Height: 0.567
  Confidence: 99.87

Parents:
   Pet
   Animal
----------

Label: Animal
Confidence: 99.87
Instances:
Parents:
----------

✓ Labels detected in dog.jpg: 5
============================================================

============================================================
SUMMARY
============================================================
Total images found: 3
Successfully processed: 3
Failed: 0
Total labels detected: 15
```

### Output Components

- **Label Name**: The detected object, scene, or concept
- **Confidence**: Confidence score (0-100) for the detection
- **Instances**: Specific occurrences with bounding box coordinates
  - **Top**: Distance from top edge (0-1, as fraction of image height)
  - **Left**: Distance from left edge (0-1, as fraction of image width)
  - **Width**: Width of bounding box (0-1, as fraction of image width)
  - **Height**: Height of bounding box (0-1, as fraction of image height)
- **Parents**: Hierarchical categories the label belongs to

## Testing

The project includes unit tests that use mocking to avoid calling actual AWS services.

### Running Tests

```powershell
# Ensure you're in the project root with venv activated
pytest tests/

# Or run with verbose output
pytest tests/ -v

# Or run a specific test file
pytest tests/test_main.py
```

### Test Coverage

The tests cover:

- Label detection functionality with mocked Boto3 responses
- Proper handling of API responses
- Count verification for detected labels

## Troubleshooting

### Common Issues

#### 1. NoCredentialsError

**Error:**

```
botocore.exceptions.NoCredentialsError: Unable to locate credentials
```

**Solution:**

- Verify AWS credentials are configured correctly
- Run `aws configure` to set up credentials
- Check that `~/.aws/credentials` file exists and contains valid credentials
- Ensure environment variables are set if using that method

#### 2. AccessDeniedException

**Error:**

```
botocore.errorfactory.AccessDeniedException: User is not authorized
```

**Solution:**

- Verify IAM user has `AmazonRekognitionFullAccess` policy
- Verify IAM user has `AmazonS3ReadOnlyAccess` policy
- Check that the S3 bucket policy allows read access
- Confirm Rekognition is available in your selected region

#### 3. NoSuchBucket

**Error:**

```
botocore.errorfactory.NoSuchBucket: The specified bucket does not exist
```

**Solution:**

- Verify bucket name is spelled correctly
- Check that the bucket exists in the specified region
- Ensure the bucket name in environment variable or script matches the actual bucket

#### 4. InvalidImageFormatException

**Error:**

```
botocore.errorfactory.InvalidImageFormatException: Request has invalid image format
```

**Solution:**

- Ensure images are valid JPEG or PNG format
- Check that files are not corrupted
- Verify file extensions match actual format
- Try re-uploading the image to S3

#### 5. No Images Found

**Output:**

```
No images found in the bucket.
```

**Solution:**

- Verify images are uploaded to S3
- Check that images have `.jpg`, `.jpeg`, or `.png` extensions (no other extensions are supported)
- Ensure images are in the root of the bucket (script doesn't search subdirectories)
- List bucket contents: `aws s3 ls s3://your-bucket-name/`

### Debugging

Enable detailed logging to diagnose issues:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
```

Test AWS connectivity:

```bash
# Test S3 access
aws s3 ls s3://your-bucket-name/

# Test Rekognition access
aws rekognition detect-labels --image "S3Object={Bucket=your-bucket-name,Name=your-image.jpg}" --region us-east-1
```

## Cost Considerations

### AWS Free Tier

**First 12 Months:**

- S3: 5 GB of standard storage
- Rekognition: 5,000 images processed per month

**Always Free:**

- None for Rekognition (limited to first 12 months)

### Pricing After Free Tier

**S3 (us-east-1):**

- Storage: ~$0.023 per GB per month
- PUT/POST requests: $0.005 per 1,000 requests
- GET requests: $0.0004 per 1,000 requests

**Rekognition:**

- Image analysis: $1.00 per 1,000 images
- First 1 million images per month: $1.00 per 1,000
- Over 1 million: reduced pricing

### Example Cost Calculation

Processing 1,000 images per month:

- Rekognition: $1.00
- S3 storage (1 GB): $0.023
- S3 GET requests: $0.0004
- **Total: ~$1.02 per month**

### Cost Optimization

- Delete processed images if no longer needed
- Use S3 lifecycle policies to transition to cheaper storage classes
- Set up AWS billing alerts
- Monitor usage with AWS Cost Explorer

## File Structure

```
rekognition_image_label_detection/
├── src/
│   ├── __init__.py          # Package initialization
│   └── main.py              # Main script with core logic
├── tests/
│   └── test_main.py         # Unit tests with mocking
├── scripts/
│   └── run.ps1              # Helper script for Windows
├── requirements.txt         # Python dependencies
└── README.md               # This documentation
```

### Key Functions in `src/main.py`

**`get_all_images_from_bucket(bucket, region_name)`**

- Lists all objects in the S3 bucket
- Filters for JPEG and PNG files
- Returns list of image keys
- Handles errors gracefully

**`detect_labels(photo, bucket, region_name, max_labels)`**

- Calls AWS Rekognition DetectLabels API
- Processes a single image
- Displays detailed label information
- Returns count of labels detected
- Includes comprehensive error handling

**`main()`**

- Entry point of the script
- Reads configuration from environment variables
- Orchestrates the image processing workflow
- Generates summary statistics

## Security Best Practices

1. **Never commit credentials to version control**

   - AWS credentials are excluded via `.gitignore`
   - Use environment variables or AWS credentials file

2. **Use IAM roles with least privilege**

   - Grant only necessary permissions
   - Avoid using root account credentials
   - Rotate access keys regularly

3. **Enable S3 bucket encryption**

   ```bash
   aws s3api put-bucket-encryption --bucket your-bucket-name \
     --server-side-encryption-configuration \
     '{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]}'
   ```

4. **Monitor AWS usage**

   - Set up CloudWatch alarms
   - Review CloudTrail logs
   - Use AWS Cost Explorer

5. **Keep dependencies updated**
   ```powershell
   pip install --upgrade boto3 botocore
   ```

## Additional Resources

- [AWS Rekognition Documentation](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html)
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)
- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS Free Tier Details](https://aws.amazon.com/free/)

## Support

For issues or questions:

- Check the [Troubleshooting](#troubleshooting) section
- Review AWS service documentation
- Open an issue in the parent repository

## License

This project uses code samples from AWS documentation. See the main repository for license information.
