# schedule-microservice

## Docker Configuration

Docker installation on AWS:

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html

Dockerfile:

```dockerfile
# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "./app.py", "--host=0.0.0.0:5003"]
```

Build docker image
```bash
docker build --tag schedule-test .
```

Run image as container
```bash
docker run --publish 5003:5003 schedule-test
```
