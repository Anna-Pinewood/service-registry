import os
from pathlib import Path

from dotenv import dotenv_values

PROJECT_PATH = Path(__file__).parent.parent

ENV_PATH = PROJECT_PATH / '.env'
config_env = dotenv_values(ENV_PATH)

SERVICE_HOST = os.environ.get('SERVICE_HOST', config_env.get("SERVICE_HOST"))
SERVICE_PORT = os.environ.get('SERVICE_PORT', config_env.get("SERVICE_PORT"))
SERVICE_NAME = os.environ.get('SERVICE_NAME', config_env.get("SERVICE_NAME"))

URL_SECRET_NUMBER = "https://lab.karpov.courses/hardml-api/module-5/get_secret_number"

SECRET_NUMBER = None
