FROM python:3.10.4

WORKDIR /app

COPY ./ /app/

ENV export PYTHONPATH="${PYTHONPATH}:/app/src/patient_account/"
ENV export PYTHONPATH="${PYTHONPATH}:/app/src"
ENV export SECRET_NUMBER="${SECRET_NUMBER}"

COPY --chown=1001:0 ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["python", "src/main.py"]