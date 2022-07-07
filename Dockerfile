FROM python

RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless && \
    apt-get clean;
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY . /myapp
WORKDIR /myapp
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]