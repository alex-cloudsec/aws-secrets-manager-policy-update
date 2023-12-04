import boto3
from botocore.exceptions import ClientError

def update_secret_policy(secret_id, policy, client):
    """
    Update the resource policy of a secret in AWS Secrets Manager.

    :param secret_id: ID or ARN of the secret to update.
    :param policy: JSON policy to apply to the secret.
    :param client: boto3 client for AWS Secrets Manager.
    :return: None
    """
    try:
        client.put_resource_policy(SecretId=secret_id, ResourcePolicy=policy)
        print(f"Policy updated for secret: {secret_id}")
    except ClientError as e:
        print(f"Error updating policy for secret {secret_id}: {e}")

def main():
    # Request AWS region input
    region = input("Please enter the AWS region: ")
    secretsmanager_client = boto3.client('secretsmanager', region_name=region)

    # Request secret ARN or 'all' input
    secret_arn = input("Please enter the ARN of the secret to update or 'all' for all secrets: ")

    # Define the policy directly in the script
    policy = '''
    {
      policy text
    }
    '''

    if secret_arn.lower() == 'all':
        # Pagination: Initialize empty token
        next_token = ''

        # Loop through all secrets, respecting pagination
        while True:
            if next_token:
                response = secretsmanager_client.list_secrets(NextToken=next_token)
            else:
                response = secretsmanager_client.list_secrets()

            secrets_list = response.get('SecretList', [])

            for secret in secrets_list:
                update_secret_policy(secret['ARN'], policy, secretsmanager_client)

            # Check if there are more secrets to fetch
            next_token = response.get('NextToken')
            if not next_token:
                break
    else:
        # Update the policy for the provided secret ARN
        update_secret_policy(secret_arn, policy, secretsmanager_client)

# Run the main function
main()
