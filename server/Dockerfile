FROM python:3.8-slim-buster

EXPOSE 8000

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY . app
WORKDIR app

RUN chmod +x ./run.sh

ENTRYPOINT ["./run.sh"]

