FROM python:3.11-slim-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg nodejs npm \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /app/

WORKDIR /app/

RUN pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir -r requirements.txt

CMD ["bash", "start"]
