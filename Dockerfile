FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN mkdir -p /var/run/postgresql/9.3-main.pg_stat_tmp
RUN chmod 0777 /var/run/postgresql/9.3-main.pg_stat_tmp
