# base image: we want our environment to come with python
FROM python:3.10-slim

# install libraries: ffmpeg, libsm6, libxext6
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

# copy requirements.txt to the image
COPY requirements.txt /

# install all libraries in requirements.txt
RUN pip3 install -r /requirements.txt

# copy the rest of the files to the image's /app directory
COPY . /app

# change working directory to /app
WORKDIR /app

# run the python script
CMD ["python3", "web_scraper.py"]