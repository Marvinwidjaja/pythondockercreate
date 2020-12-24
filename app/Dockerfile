# base image
FROM python:3.7

# set workdir
COPY . /app

# add files from your current directory
WORKDIR /app

# run some bash command
RUN pip install -r requirements.txt

# port number the container should expose to outside
EXPOSE 8080

# run the application
ENTRYPOINT python main.py
