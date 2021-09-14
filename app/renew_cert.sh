#!/bin/bash

SLL_URL=https://noharm.ai/ssl

wget -q $SLL_URL/fullchain.pem -O /etc/ssl/fullchain.pem --no-check-certificate
wget -q $SLL_URL/privkey.pem -O /etc/ssl/privkey.pem --no-check-certificate
wget -q $SLL_URL/ssl-dhparams.pem -O /etc/ssl/ssl-dhparams.pem --no-check-certificate

/usr/sbin/service nginx reload