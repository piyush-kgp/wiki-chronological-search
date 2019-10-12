
FROM python:3.7-slim-buster

COPY ./static /static/
COPY ./templates /templates/
COPY ./app.py /app.py
COPY ./chronological_search.py /chronological_search.py
COPY ./requirements.txt /requirements.txt

RUN apt-get update
RUN apt-get install -y gcc
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python","app.py"]
