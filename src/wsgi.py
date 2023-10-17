
from patient_account.consts import SERVICE_PORT
import signal
from graceful_shutdown import signal_handler
from main import run_app
signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

workers = 2
# worker_connections = 100
threads = 10
timeout = 10000
bind = f'0.0.0.0:{SERVICE_PORT}'
