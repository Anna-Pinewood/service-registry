Before start `main.py`` create `.env` file with redis password. Use `.env_example` as template.

To run with gunicorn:
`poetry run gunicorn -c src/wsgi.py  --pid ~/workspace/service-registry/gunicorn.pid 'src.wsgi:run_app()'`

To run as it is:
`poetry run python src/main.py`