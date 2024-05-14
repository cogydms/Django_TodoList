FROM python:3.12-alpine
RUN pip3 install Django
RUN apk add gcc musl-dev

COPY . /app
WORKDIR /app
RUN python3 -m venv venv && . venv/bin/activate
RUN pip3 install -r requirement.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000