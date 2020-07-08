FROM python:3.8-slim-buster

EXPOSE 8000

COPY . app
WORKDIR app

RUN chmod +x ./run.sh

RUN pip install -r ./requirements.txt

ENTRYPOINT ["./run.sh"]

