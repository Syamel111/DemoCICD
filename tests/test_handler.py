import sys
import os
import json
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from lambda_function import handler

@patch("boto3.client")
def test_handler_returns_200(mock_boto_client, monkeypatch):
    monkeypatch.setenv("SECRETS_NAME", "dummy-secret-name")

    mock_secrets_client = MagicMock()
    mock_secrets_client.get_secret_value.return_value = {
        "SecretString": '{"test_key": "test_value"}'
    }
    mock_boto_client.return_value = mock_secrets_client

    event = {"httpMethod": "GET"}
    context = {}
    response = handler(event, context)

    assert response["statusCode"] == 200

    body = json.loads(response["body"])
    assert body["message"] == "Resume API v1"
    assert body["region"] == "ap-southeast-1"
    assert json.loads(body["secret"]) == {"test_key": "test_value"}
