FROM python:3.10.4

WORKDIR /app

COPY ./ /app/src/

COPY --chown=1001:0 ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["python", "main.py"]