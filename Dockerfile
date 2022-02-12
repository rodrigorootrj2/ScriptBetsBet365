FROM python
RUN apt-get update && apt-get install default-mysql-client python3 python3-pip -y && apt-get clean
RUN mkdir /opt/app

ARG API-TOKEN


COPY app/ /opt/app
RUN pip install -r /opt/app/requirements.txt
WORKDIR /opt/
CMD python3 /opt/app/run.py