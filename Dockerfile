FROM python:3.13

WORKDIR /wipapp
COPY . /wipapp

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "--workers", "2", "--threads", "8", "app:application"]