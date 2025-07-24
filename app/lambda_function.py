import boto3
import json
import os


def handler(event, context):
    secrets_client = boto3.client('secretsmanager')
    secret = secrets_client.get_secret_value(
        SecretId=os.environ['SECRETS_NAME']
    )

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Resume API v1',
            'region': 'ap-southeast-1',
            # Just for demo; remove in real app
            'secret': secret['SecretString']
        })
    }
