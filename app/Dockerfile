# Init container
FROM python:3.10
WORKDIR ./app

# Requirements
RUN python3 -m pip install --upgrade pip
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

# Run server
COPY . .
RUN chmod +x migrate.sh
ENTRYPOINT bash migrate.sh && gunicorn -c gunicorn.py app:app
