FROM python:3.6-slim

LABEL Name=weather Version=0.0.1
EXPOSE 8000

WORKDIR /app
ADD ./src/weather /app
ADD ./requirements.txt /tmp/requirements.txt

# Install libpq-dev and app requirements
RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    python3 -m pip install -r /tmp/requirements.txt && \
    apt-get purge -y gcc && \
    apt-get autoremove -y
