# AWS Projects

A collection of AWS service demonstrations and mini-projects organized in a single repository. Each project showcases different AWS services and best practices for cloud development.

## 📋 Repository Structure

This repository follows a multi-project layout where each mini-project is self-contained under the `projects/` directory:

```text
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

See [PROJECTS.md](PROJECTS.md) for a complete list of available projects and quick start commands.

### Available Projects

1. **Rekognition Image Label Detection** - Batch processing of images using Amazon Rekognition

---

## 📦 General Prerequisites

- Python 3.7 or higher
- An AWS account with appropriate IAM permissions
- AWS CLI configured (or credentials via environment variables)
- Basic knowledge of AWS services

## �️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/JerrySoPro/AWS-Projects.git
cd AWS-Projects
```

### 2. Choose a Project

Browse the `projects/` directory and select a project you want to run. Each project is self-contained with its own:

- `README.md` — Project-specific documentation and setup instructions
- `requirements.txt` — Python dependencies
- `src/` — Source code
- `tests/` — Unit tests (when applicable)
- `scripts/` — Helper scripts (optional)

### 3. Follow Project-Specific Instructions

Navigate to the project folder and follow the README:

```powershell
Set-Location -LiteralPath "./projects/[project-name]"
# Read the README.md for specific setup and run instructions
```

---

## � AWS Setup (General)

Most projects in this repository require basic AWS configuration. Here's how to set up your AWS environment:

### Step 1: Create an AWS Account

1. Go to [AWS Console](https://aws.amazon.com/)
2. Click **"Create an AWS Account"**
3. Follow the registration process
4. Provide payment information (free tier available)
5. Verify your identity

### Step 2: Configure AWS CLI

#### Install AWS CLI

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

#### Configure Credentials

Run the following command and enter your credentials:

```bash
aws configure
```

You'll be prompted to enter:

```text
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

### Step 3: Create IAM User and Access Keys

1. **Navigate to IAM**
   - In AWS Console search bar, type "IAM"
   - Click on **"IAM"** (Identity and Access Management)

2. **Create a New User**
   - Click **"Users"** in the left sidebar
   - Click **"Create user"**
   - Enter username (e.g., `aws-projects-user`)
   - Click **"Next"**

3. **Set Permissions**
   - Select **"Attach policies directly"**
   - Choose policies based on the project you're running
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
   - Click **"Create access key"**
   - **⚠️ IMPORTANT**: Save both Access Key ID and Secret Access Key
   - Click **"Download .csv file"** for safekeeping
   - Click **"Done"**

---

## 🔒 Security Best Practices

1. **Never commit credentials to Git**
   - The repository includes a `.gitignore` for sensitive files
   - Use environment variables or AWS credentials file
   - Keep `.env` files local only

2. **Use IAM roles with least privilege**
   - Only grant necessary permissions for each project
   - Avoid using root account credentials
   - Rotate access keys regularly

3. **Enable MFA on your AWS account**
   - Add an extra layer of security
   - Especially important for production accounts

4. **Monitor AWS usage and costs**
   - Set up billing alerts
   - Use AWS Cost Explorer
   - Review charges regularly

---

## 💰 Cost Considerations

Most projects in this repository are designed to work within AWS Free Tier limits. However, always:

- Monitor your AWS usage
- Set up billing alerts
- Review each project's README for specific cost information
- Clean up resources after testing

### AWS Free Tier Highlights

- **First 12 months**: Many services offer free tier limits
- **Always Free**: Some services have perpetual free tier
- **Free Trials**: Limited-time trials for certain services

See [AWS Free Tier](https://aws.amazon.com/free/) for details.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add a new AWS mini-project:

1. Fork the repository
2. Create a new folder under `projects/`
3. Follow the standard project structure
4. Add comprehensive README with setup instructions
5. Submit a pull request

---

## 📚 Additional Resources

- [AWS Documentation](https://docs.aws.amazon.com/)
- [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS CLI Documentation](https://docs.aws.amazon.com/cli/)
- [AWS Free Tier](https://aws.amazon.com/free/)

---

## 📄 License

This repository contains projects with various licenses. See individual project folders for specific license information.

---

## 📧 Support

If you encounter any issues:

1. Check the project-specific README
2. Review AWS service documentation
3. Open an issue on GitHub

---

**Happy Cloud Computing! ☁️**
