FROM python:3.12-alpine

WORKDIR /multiport-webserver
COPY app.py /multiport-webserver

ENTRYPOINT ["python3","/multiport-webserver/app.py"]
