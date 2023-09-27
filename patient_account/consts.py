import os
from pathlib import Path

from dotenv import dotenv_values

PROJECT_PATH = Path(__file__).parent.parent

ENV_PATH = PROJECT_PATH / '.env'
config_env = dotenv_values(ENV_PATH)

print('env file:\n', config_env)
print('SERVICE_HOST from ENV VAR:\n', os.environ.get("SERVICE_POR"))

SERVICE_HOST = os.environ.get('SERVICE_HOST', config_env.get("SERVICE_HOST"))
SERVICE_PORT = os.environ.get('SERVICE_PORT', config_env.get("SERVICE_PORT"))

URL_SECRET_NUMBER = "https://lab.karpov.courses/hardml-api/module-5/get_secret_number"

SECRET_NUMBER = None
