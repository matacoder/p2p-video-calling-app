FROM python:3.10-slim-buster

WORKDIR /app

COPY fastapi_server/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3000

WORKDIR /app/fastapi_server

CMD [ "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "3000", "--reload"]
