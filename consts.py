from pathlib import Path

from dotenv import dotenv_values

PROJECT_PATH = Path(__file__).parent

ENV_PATH = PROJECT_PATH / '.env'
config_env = dotenv_values(ENV_PATH)

REDIS_HOST = '65.21.147.64'
REDIS_PORT = '6379'
REDIS_PASSWORD = config_env.get("REDIS_PASSWORD")

URL_SECRET_NUMBER = "https://lab.karpov.courses/hardml-api/module-5/get_secret_number"

SECRET_NUMBER = None