FROM python:3.10-slim-buster

WORKDIR /app

COPY aiohttp_server/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3000

CMD [ "python3", "aiohttp_server/server.py"]
