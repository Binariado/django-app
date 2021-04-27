# set base image (host OS)
FROM python:3.9
  ENV PYTHONUNBUFFERED 1  
  
  RUN apt-get update && apt-get install -y supervisor && apt-get install -y cron

  RUN mkdir -p /var/log/supervisor

  COPY config/etc/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
  RUN mkdir /config  
 
  COPY requirements.txt /config/requirements.txt 
  RUN pip install -r /config/requirements.txt
  RUN mkdir /app_django
  COPY . /app_django/

  # make script executable
  RUN chmod +x /app_django/scheduler.py

  WORKDIR /app_django

  CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]