#legacy_bot/DockerFile

FROM python:2.7-slim

LABEL authors="lkris"

WORKDIR /app
COPY .. /app

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]