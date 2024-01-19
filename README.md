# AWS Secrets Manager Policy Updater

## Overview
This Python script is designed to update the resource policy of secrets stored in AWS Secrets Manager. It allows users to either update the policy of a specific secret (using its ARN) or apply a policy update to all secrets within the specified AWS region.

## Features
- Update the resource policy of a specific secret in AWS Secrets Manager.
- Apply a policy update to all secrets within a specified AWS region.
- Utilizes Boto3, the AWS SDK for Python.

## Prerequisites
- Python 3.x
- Boto3 library installed (`pip install boto3`).
- AWS CLI installed and configured with appropriate permissions.
- AWS account with access to AWS Secrets Manager.

## Usage
1. **Setup**: Ensure your AWS CLI is configured with the necessary permissions to interact with AWS Secrets Manager.
2. **Run the Script**: Execute the script in a Python environment. You will be prompted to enter:
   - The AWS region where your secrets are managed.
   - The ARN of the specific secret to update or 'all' to update all secrets in the region.
   - Ensure that the policy JSON is correctly defined within the script before execution.
3. **View Results**: The script outputs the status of the policy update for each secret.
