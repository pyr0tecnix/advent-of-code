# 1. Base image
FROM python:3.10.0-slim-buster

# 2. Copy files
COPY . .

# 3. Install dependencies
# RUN pip install -r /src/requirements.txt

WORKDIR /src

