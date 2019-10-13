
FROM python:3.7-slim-buster
COPY ./webapp /webapp/
RUN apt-get update
RUN apt-get install -y gcc
RUN pip install -r /webapp/requirements.txt
CMD cd /webapp && gunicorn --bind 0.0.0.0:$PORT wsgi

# For testing on local before deployment use below line, (heroku sets the port variable by itself)
# CMD cd /webapp && gunicorn --bind 0.0.0.0:8000 wsgi
