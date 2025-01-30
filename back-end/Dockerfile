FROM python:3.11-slim

WORKDIR /app
COPY ./app/ /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

