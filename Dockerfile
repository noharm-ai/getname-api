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

RUN apt-get install -y openssl && \
    openssl genrsa -des3 -passout pass:flaskapi -out server.pass.key 2048 && \
    openssl rsa -passin pass:flaskapi -in server.pass.key -out /etc/ssl/server.key && \
    rm server.pass.key && \
    openssl req -new -key /etc/ssl/server.key -out /etc/ssl/server.csr \
        -subj "/C=UK/ST=Warwickshire/L=Leamington/O=OrgName/OU=IT Department/CN=example.com"  && \
    openssl x509 -req -days 365  -in /etc/ssl/server.csr -signkey /etc/ssl/server.key -out /etc/ssl/server.crt

COPY tmp.conf /etc/nginx/conf.d/tmp.conf

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

COPY ./app /app