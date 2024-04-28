FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
# Install Python 3.9 and pip
RUN apt-get update && \
    apt-get install -y python3.9 python3-pip && \
    apt-get clean

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY Codex/palindrome.py /app/palindrome.py

# Set the default command to run when the container starts
CMD ["bash"]
