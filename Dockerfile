FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y python3.9 python3-pip && \
    apt-get clean


WORKDIR /app

COPY Codex/palindromeNumber_easy.py /app/palindromeNumber_easy.py

CMD ["bash"]
