from flask import Flask

from consts import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT
from patient_account import init_redis_connection
from patient_account import views

app = Flask(__name__)


if __name__ == "__main__":
    init_redis_connection(host=REDIS_HOST,
                          port=REDIS_PORT,
                          password=REDIS_PASSWORD)
    app.register_blueprint(views.bp)
    app.run()
