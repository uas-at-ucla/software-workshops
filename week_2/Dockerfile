FROM python:3.10-slim

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /app
WORKDIR /app

# NEW: run our script to start gunicorn
# when the Docker container spins up
CMD ["./start_gunicorn.sh"]