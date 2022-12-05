FROM python:3.10.8-buster
ENV BOT_NAME=$BOT_NAME

WORKDIR /usr/src/app/${BOT_NAME}

COPY requirements.txt /usr/src/app/${BOT_NAME}
RUN pip3 install -r /usr/src/app/${BOT_NAME}/requirements.txt

# USED TO PREVENT THE CONNECTION DISCONNECTING IN THE EVENT OF AN UNEXPECTED ERROR
# ERROR: Persistent timestamp empty
RUN apt-get update -y && apt-get install vim -y
RUN vim /usr/local/lib/python3.10/site-packages/telethon/client/updates.py -c ":400,400d|:wq"

COPY . /usr/src/app/${BOT_NAME}