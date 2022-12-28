FROM tiangolo/uwsgi-nginx-flask:python3.8

# if apt-secure(8) error use --allow-releaseinfo-change
RUN apt-get update

RUN apt-get update && apt-get install -y cron


# Copy crontab file to the cron.d directory
COPY crontab /etc/cron.d/crontab

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/crontab

# Apply cron job
RUN crontab /etc/cron.d/crontab

ARG SLL_URL=https://noharm.ai/ssl

RUN wget -c $SLL_URL/fullchain.pem -P /etc/ssl --no-check-certificate
RUN wget -c $SLL_URL/privkey.pem -P /etc/ssl --no-check-certificate
RUN wget -c $SLL_URL/ssl-dhparams.pem -P /etc/ssl --no-check-certificate

COPY tmp.conf /etc/nginx/conf.d/tmp.conf

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

COPY ./app /app

# Create the log file if needed for debug, uncomment crontab file as well
# RUN touch /var/log/cron.log

# Give execution rights on the task script
RUN chmod 0744 /app/renew_cert.sh
