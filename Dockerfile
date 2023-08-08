
FROM python:3.8

RUN apt-get update && apt-get install -y build-essential

RUN pip install django

COPY two .

RUN cd two

RUN python3 manage.py migrate

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
