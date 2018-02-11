FROM python:3.6.3-jessie

# Setup Project Dir
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install Python Dependencies
COPY ./server/requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

# Add the sourcecode
COPY ./server /usr/src/app

# Start the app at port 5000
EXPOSE 5000
CMD [ "gunicorn", "server:app", "-b 0.0.0.0:5000", "-t 60"]
