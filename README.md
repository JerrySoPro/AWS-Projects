# AWS Mini Projects

A collection of AWS service demonstrations and mini-projects organized in a single repository.

## 📋 Repository Structure

This repository follows a multi-project layout where each mini-project is self-contained under the `projects/` directory:

```
├── projects/
│   ├── rekognition_image_label_detection/
│   │   ├── src/
│   │   ├── tests/
│   │   ├── requirements.txt
│   │   └── README.md
│   └── [future projects...]
├── PROJECTS.md          # Quick index of all projects
└── README.md            # This file
```

## 🚀 Current Projects

### 1. Rekognition Image Label Detection

**Location**: `projects/rekognition_image_label_detection/`

A Python script that automatically detects labels in images stored in an AWS S3 bucket using Amazon Rekognition service.

**Features**:

- Batch processing of all images in an S3 bucket
- Error handling for invalid images
- Detailed output with confidence scores and bounding boxes
- Summary report with success/failure statistics
- Supports JPEG and PNG formats

**Quick start**:

```powershell
Set-Location -LiteralPath "./projects/rekognition_image_label_detection/src"
python main.py
```

See the [project README](projects/rekognition_image_label_detection/README.md) for detailed setup instructions.

---

## 📦 General Prerequisites

- Python 3.7 or higher
- An AWS account with appropriate IAM permissions
- AWS CLI configured (or credentials via environment variables)
- Basic knowledge of AWS services

## 🚀 Getting Started

Each project contains:

- `README.md` — Project-specific documentation and setup
- `requirements.txt` — Python dependencies
- `src/` — Source code
- `tests/` — Unit tests (when applicable)
- `scripts/` — Helper scripts (optional)

Refer to each project's README for detailed instructions.

---

## 📋 Original Documentation (for Rekognition project)

### Table of Contents

- [AWS Setup](#aws-setup)
  - [Step 1: Create an AWS Account](#step-1-create-an-aws-account)
  - [Step 2: Create an S3 Bucket](#step-2-create-an-s3-bucket)
  - [Step 3: Upload Images](#step-3-upload-images-to-s3)
  - [Step 4: Create IAM User and Access Keys](#step-4-create-iam-user-and-access-keys)
  - [Step 5: Configure AWS CLI](#step-5-configure-aws-cli)
- [Troubleshooting](#troubleshooting)
- [Cost Considerations](#cost-considerations)
- [License](#license)

## 🔍 Overview

This script automatically:

- Lists all images in your specified S3 bucket
- Processes each image with AWS Rekognition
- Detects objects, scenes, activities, and concepts in images
- Provides confidence scores and bounding box coordinates
- Generates a comprehensive summary report

---

## 🚀 AWS Setup (for Rekognition project)

### Step 1: Create an AWS Account

1. Go to [AWS Console](https://aws.amazon.com/)
2. Click **"Create an AWS Account"**
3. Follow the registration process
4. Provide payment information (free tier available)
5. Verify your identity

### Step 2: Create an S3 Bucket

#### Using AWS Console (Web Interface):

1. **Sign in to AWS Console**

   - Go to https://console.aws.amazon.com/
   - Sign in with your credentials

2. **Navigate to S3**

   - In the search bar at the top, type "S3"
   - Click on **"S3"** from the results

3. **Create Bucket**

   - Click the **"Create bucket"** button
   - Enter a unique bucket name (e.g., `project-rekognition-s3`)
     - Bucket names must be globally unique
     - Use lowercase letters, numbers, and hyphens only
   - Select your **AWS Region** (e.g., `us-east-1`)
   - Leave other settings as default (or configure as needed)
   - Scroll down and click **"Create bucket"**

4. **Configure Bucket (Optional)**
   - You can leave default settings for testing
   - For production, consider enabling:
     - Versioning
     - Encryption
     - Access logging

#### Using AWS CLI:

```bash
aws s3 mb s3://YOUR_BUCKET_NAME --region us-east-1
```

### Step 3: Upload Images to S3

#### Using AWS Console:

1. **Open your bucket**

   - Click on your bucket name from the S3 dashboard

2. **Upload files**
   - Click the **"Upload"** button
   - Click **"Add files"** or drag and drop images
   - Select your JPEG or PNG images
   - Click **"Upload"** at the bottom

#### Using AWS CLI:

```bash
# Upload a single file
aws s3 cp /path/to/your/image.png s3://YOUR_BUCKET_NAME/

# Upload multiple files from a folder
aws s3 cp /path/to/images/ s3://YOUR_BUCKET_NAME/ --recursive --exclude "*" --include "*.jpg" --include "*.png"
```

### Step 4: Create IAM User and Access Keys

1. **Navigate to IAM**

   - In AWS Console search bar, type "IAM"
   - Click on **"IAM"** (Identity and Access Management)

2. **Create a New User**

   - Click **"Users"** in the left sidebar
   - Click **"Create user"**
   - Enter username (e.g., `rekognition-user`)
   - Click **"Next"**

3. **Set Permissions**

   - Select **"Attach policies directly"**
   - Search and select these policies:
     - `AmazonS3ReadOnlyAccess` (to read images from S3)
     - `AmazonRekognitionFullAccess` (to use Rekognition)
   - Click **"Next"**
   - Click **"Create user"**

4. **Create Access Keys**
   - Click on the newly created user
   - Go to **"Security credentials"** tab
   - Scroll to **"Access keys"** section
   - Click **"Create access key"**
   - Select **"Command Line Interface (CLI)"**
   - Check the confirmation box
   - Click **"Next"**
   - (Optional) Add a description tag
   - Click **"Create access key"**
   - **⚠️ IMPORTANT**: Save both:
     - Access Key ID
     - Secret Access Key
     - (You won't be able to see the secret key again!)
   - Click **"Download .csv file"** for safekeeping
   - Click **"Done"**

### Step 5: Configure AWS CLI

#### Install AWS CLI:

**Windows:**

```powershell
# Download and install from:
# https://awscli.amazonaws.com/AWSCLIV2.msi
```

**macOS:**

```bash
brew install awscli
```

**Linux:**

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

#### Configure Credentials:

Run the following command and enter your credentials:

```bash
aws configure
```

You'll be prompted to enter:

```
AWS Access Key ID [None]: YOUR_ACCESS_KEY_ID
AWS Secret Access Key [None]: YOUR_SECRET_ACCESS_KEY
Default region name [None]: us-east-1
Default output format [None]: json
```

**Alternative: Manual Configuration**

Create/edit `~/.aws/credentials` (Linux/Mac) or `C:\Users\USERNAME\.aws\credentials` (Windows):

```ini
[default]
aws_access_key_id = YOUR_ACCESS_KEY_ID
aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```

Create/edit `~/.aws/config`:

```ini
[default]
region = us-east-1
output = json
```

---

## 📖 Per-Project Setup (Rekognition)

For the Rekognition Image Label Detection project, see the [project README](projects/rekognition_image_label_detection/README.md) for:

- Installation steps
- Configuration (bucket name, region)
- Usage examples
- Output samples

Quick reference for running the project:

```powershell
# Navigate to the project source folder
Set-Location -LiteralPath "./projects/rekognition_image_label_detection/src"

# Run the script (ensure AWS credentials are configured)
python main.py
```

---

## Output Example (Rekognition)

```
Fetching images from bucket: project-rekognition-s3
Found 3 image(s) in the bucket
Files: image1.jpg, image2.png, photo.jpeg
============================================================

============================================================
Detected labels for image1.jpg

Label: Dog
Confidence: 99.8765432
Instances:
  Bounding box
    Top: 0.123456
    Left: 0.234567
    Width: 0.456789
    Height: 0.567890
  Confidence: 99.8765432

Parents:
   Pet
   Animal
----------

Label: Animal
Confidence: 99.8765432
Instances:
Parents:
----------

✓ Labels detected in image1.jpg: 10
============================================================

============================================================
SUMMARY
============================================================
Total images found: 3
Successfully processed: 3
Failed: 0
Total labels detected: 30
```

## 🔧 Troubleshooting

### Common Issues

#### 1. **InvalidImageFormatException**

**Error:**

```
botocore.errorfactory.InvalidImageFormatException: Request has invalid image format
```

**Solutions:**

- Ensure images are valid JPEG or PNG format
- Check that files aren't corrupted
- Verify files have correct extensions
- Try re-uploading the image to S3

#### 2. **AccessDeniedException**

**Error:**

```
botocore.errorfactory.AccessDeniedException: User is not authorized
```

**Solutions:**

- Verify IAM user has correct permissions
- Check that access keys are configured correctly
- Ensure S3 bucket policy allows access
- Confirm Rekognition service is available in your region

#### 3. **NoSuchBucket**

**Error:**

```
botocore.errorfactory.NoSuchBucket: The specified bucket does not exist
```

**Solutions:**

- Verify bucket name is spelled correctly
- Check that bucket exists in the correct region
- Ensure bucket name matches in the script

#### 4. **NoCredentialsError**

**Error:**

```
botocore.exceptions.NoCredentialsError: Unable to locate credentials
```

**Solutions:**

- Run `aws configure` to set up credentials
- Verify credentials file exists in `~/.aws/credentials`
- Check environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`

#### 5. **No images found in the bucket**

**Solutions:**

- Verify images are uploaded to S3
- Check that images have `.jpg`, `.jpeg`, or `.png` extensions
- Ensure images are in the root of the bucket (not in subfolders)
- Modify script to support subfolders if needed

### Debugging Tips

**Enable boto3 logging:**

```python
import logging

logging.basicConfig(level=logging.DEBUG)
```

**Test AWS CLI connectivity:**

```bash
# List S3 buckets
aws s3 ls

# List objects in your bucket
aws s3 ls s3://project-rekognition-s3/

# Test Rekognition
aws rekognition detect-labels --image "S3Object={Bucket=YOUR_BUCKET_NAME,Name=your_image.jpg}" --region us-east-1
```

## Cost Considerations

### AWS Free Tier (First 12 Months)

- **S3**: 5 GB of standard storage
- **Rekognition**: 5,000 images per month for first 12 months

### After Free Tier

- **S3 Storage**: ~$0.023 per GB per month (us-east-1)
- **S3 Requests**: $0.0004 per 1,000 GET requests
- **Rekognition**: $1.00 per 1,000 images processed

### Example Cost Calculation

Processing 1,000 images per month:

- Rekognition: ~$1.00
- S3 Storage (assuming 1GB): ~$0.023
- S3 Requests: ~$0.0004
- **Total: ~$1.02 per month**

### Cost Optimization Tips

1. Delete processed images from S3 if not needed
2. Use S3 lifecycle policies to move to cheaper storage
3. Batch process images instead of individual processing
4. Monitor usage with AWS Cost Explorer

## Script Breakdown

### Functions Overview

#### `get_all_images_from_bucket(bucket)`

- Lists all objects in the S3 bucket
- Filters for JPEG and PNG files only
- Returns list of image filenames
- Handles errors gracefully

#### `detect_labels(photo, bucket)`

- Calls AWS Rekognition DetectLabels API
- Processes a single image
- Prints detailed label information
- Returns count of labels detected
- Includes error handling

#### `main()`

- Entry point of the script
- Coordinates the entire workflow
- Generates summary statistics

## Security Best Practices

1. **Never commit credentials to GitHub**

   - Add `.aws/` and `credentials` to `.gitignore`
   - Use environment variables or AWS credentials file

2. **Use IAM roles with least privilege**

   - Only grant necessary permissions
   - Avoid using root account credentials

3. **Enable S3 bucket encryption**

   ```bash
   aws s3api put-bucket-encryption --bucket project-rekognition-s3 --server-side-encryption-configuration '{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]}'
   ```

4. **Enable S3 versioning** (for backup)

   ```bash
   aws s3api put-bucket-versioning --bucket project-rekognition-s3 --versioning-configuration Status=Enabled
   ```

5. **Rotate access keys regularly**

## Requirements File

Create a `requirements.txt` file:

```txt
boto3>=1.26.0
botocore>=1.29.0
```

## Project Structure

```
aws-rekognition-label-detection/
├── AWS rekognition.py    # Main script
├── README.md             # This file
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore file
└── LICENSE              # License file
```

## .gitignore

Create a `.gitignore` file to exclude sensitive information:

```gitignore
# AWS Credentials
.aws/
credentials
config

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
dist/
*.egg-info/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Review [AWS Rekognition Documentation](https://docs.aws.amazon.com/rekognition/)
3. Open an issue on GitHub

## Additional Resources

- [AWS Rekognition Developer Guide](https://docs.aws.amazon.com/rekognition/latest/dg/what-is.html)
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)
- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS CLI Documentation](https://docs.aws.amazon.com/cli/)

## License

Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
PDX-License-Identifier: MIT-0

For details, see [https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE](https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE)

---

**by peace**
