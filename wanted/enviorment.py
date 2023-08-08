import json

import boto3
from dotenv import load_dotenv


def get_secret(env: str):

    env_file = f".env.{env}"

    secret_name = f"{env}/wanted"
    region_name = "ap-northeast-2"

    try:
        client = boto3.client(service_name="secretsmanager", region_name=region_name)
        response = client.get_secret_value(SecretId=secret_name)
        secret = json.loads(response["SecretString"])

        with open(env_file, "w") as f:
            for k, v in secret.items():
                f.write(f"{k}={v}\n")

    # 이후 로깅 처리 예정
    except Exception as e:
        raise e

    finally:
        load_dotenv(env_file)
