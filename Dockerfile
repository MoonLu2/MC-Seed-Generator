FROM ubuntu:22.04

ADD seeds.py /seeds/

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install flask

EXPOSE 5001

ENTRYPOINT ["python3", "/seeds/seeds.py"]

