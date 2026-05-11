FROM python:3.14-slim

WORKDIR /app

COPY requiremnts.txt .
RUN pip isntall -r requiremnts.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
