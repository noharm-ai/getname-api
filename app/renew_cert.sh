#!/bin/bash

SLL_URL=${GETNAME_SLL_URL}

wget -q $SLL_URL/fullchain.pem -O /etc/ssl/fullchain.pem --no-check-certificate
wget -q $SLL_URL/privkey.pem -O /etc/ssl/privkey.pem --no-check-certificate
wget -q $SLL_URL/ssl-dhparams.pem -O /etc/ssl/ssl-dhparams.pem --no-check-certificate

/usr/sbin/service nginx reload
