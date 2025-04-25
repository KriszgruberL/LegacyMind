# ai-brain/Dockerfile

FROM python:3.13-slim
LABEL authors="lkris"

RUN apt-get update && apt-get install -y \
    build-essential \
    g++ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "ai_app.py"]