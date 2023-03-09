FROM debian:stable
LABEL maintainer="s@mck.la"

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    ntp python3 pip\
    && mkdir -p /opt/generate-mimecast-key
ADD run.py main.py /opt/generate-mimecast-key/
RUN pip3 install fastapi uvicorn["standard"]
WORKDIR /opt/generate-mimecast-key


VOLUME ["/opt/generate-mimecast-key"]

ENTRYPOINT /usr/bin/python3 -u /opt/generate-mimecast-key/run.py

EXPOSE 8000/tcp
