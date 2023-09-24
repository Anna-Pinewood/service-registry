from flask import Flask

from consts import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT
from patient_account import init_redis_connection, init_scheduler
from patient_account import views
from patient_account.service_discover import register

app = Flask(__name__)


if __name__ == "__main__":
    init_redis_connection(host=REDIS_HOST,
                          port=REDIS_PORT,
                          password=REDIS_PASSWORD)
    service_name = "web_app"
    scheduler = init_scheduler(service_name=service_name)
    # import patient_account.load_balancing as load_balancing
    # print(load_balancing.cycle_to_list(load_balancing.replicas_pool))
    scheduler.init_app(app)
    scheduler.start()

    app.register_blueprint(views.bp)
    app.run()

    with app.test_request_context('/return_secret_number'):
    # Вызовите обработчик напрямую
        response = app.full_dispatch_request()
    if response.status_code == 200:
        data = response.get_json()
        secret_number = data.get('secret_number')
        register(service_name)