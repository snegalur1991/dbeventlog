FROM python:3.10-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /opt/appdata
COPY packages packages
RUN apt-get -y update
RUN apt-get install -y gcc default-libmysqlclient-dev netcat
RUN pip3 install -r packages

COPY . .

EXPOSE 8000

ENTRYPOINT ["/opt/appdata/entrypoint.sh"]
