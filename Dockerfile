FROM python:3.8-slim-buster

LABEL authors="Luca Cavalcante"

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN python manage.py migrate

RUN python init_db.py

ENTRYPOINT ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]