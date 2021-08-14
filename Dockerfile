FROM tiangolo/uwsgi-nginx-flask:python3.8

RUN apt-get update

RUN pip install cx-Oracle \
    && mkdir -p /opt/oracle \
    && cd /opt/oracle \
    && wget https://download.oracle.com/otn_software/linux/instantclient/199000/instantclient-basic-linux.x64-19.9.0.0.0dbru.zip --no-check-certificate \
    && unzip instantclient-basic-linux.x64-19.9.0.0.0dbru.zip \
    && apt-get install -y libaio1 libaio-dev \
    && sh -c "echo /opt/oracle/instantclient_19_9 > /etc/ld.so.conf.d/oracle-instantclient.conf" \
    && ldconfig
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_19_9

ARG SLL_URL=https://noharm.ai/ssl

RUN wget -c $SLL_URL/fullchain.pem -P /etc/ssl --no-check-certificate
RUN wget -c $SLL_URL/privkey.pem -P /etc/ssl --no-check-certificate
RUN wget -c $SLL_URL/ssl-dhparams.pem -P /etc/ssl --no-check-certificate

COPY tmp.conf /etc/nginx/conf.d/tmp.conf

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

COPY ./app /app