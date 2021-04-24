# set base image (host OS)
FROM python:3.9

# working directory
WORKDIR /app_django
# dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy content to the working directory
COPY / .

# command to run on container start
CMD [ "python", "./manage.py", "runserver" ]