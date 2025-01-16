FROM python:3.12

WORKDIR /wip
COPY . /wip

RUN pip install --upgrade pip
RUN pip install requests flask python-dotenv sqlalchemy uuid cloud-sql-python-connector[pymysql] gunicorn

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "--workers", "2", "--threads", "8", "app:application"]