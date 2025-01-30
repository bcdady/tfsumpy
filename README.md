# TFSumPy - Terraform Plan Analyzer

TFSumPy is a Python-based tool that analyzes Terraform plan files to provide a clear summary of infrastructure changes and identify potential risks. It helps DevOps teams review infrastructure changes more effectively by:

- Summarizing resource changes (create, update, delete)
- Identifying high and medium risk changes
- Automatically redacting sensitive information
- Providing detailed resource-level reporting

## Features

- 🔍 Analyzes Terraform plan JSON output
- ⚠️ Identifies high-risk changes (deletions of critical resources, security group modifications)
- 🔒 Automatically redacts sensitive information (credentials, IPs, resource names)
- 📊 Provides clear summary statistics
- 🛡️ Supports both pre and post Terraform 0.12 plan formats

## Installation

Currently, TFSumPy can only be installed from source:

```bash
git clone https://github.com/notry-cloud/tfsumpy.git
cd tfsumpy
pip install .
```

## Usage

```bash
terraform plan -out=tfplan
terraform show -json tfplan > plan.json
````

```bash
tfsumpy -i plan.json

Infrastructure Change Analysis
==============================
Total Changes: 5
Create: 2
Update: 2
Delete: 1

Risk Assessment:

High Risks:
- High risk: Security-related configuration change
Medium Risks:
 - Medium risk: Version change could cause compatibility issues
Resource Details:
- CREATE aws_s3_bucket: project-storage-[REDACTED]
- UPDATE aws_security_group: app-sg-[REDACTED]
- UPDATE aws_ecs_service: api-service
- DELETE aws_iam_role: legacy-role
- CREATE aws_lambda_function: processor-function

```

## Requirements

- Python 3.7 or higher
- Terraform 0.12 or higher (for plan generation)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
