# getName-api
getName Api to resolve patient's name

### 1. Install

```
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

### Install Oracle Cli

Link from https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html

```
sudo mkdir /opt/oracle
cd /opt/oracle

wget https://download.oracle.com/otn_software/linux/instantclient/199000/instantclient-basic-linux.x64-19.9.0.0.0dbru.zip

unzip instantclient-basic-linux.x64-19.9.0.0.0dbru.zip
sudo apt install libaio-dev
sudo sh -c "echo /opt/oracle/instantclient_19_9 >/etc/ld.so.conf.d/oracle-instantclient.conf"
sudo ldconfig
export LD_LIBRARY_PATH=/opt/oracle/instantclient_19_9:$LD_LIBRARY_PATH
```

Tutorial from: https://docs.oracle.com/en/database/oracle/oracle-database/19/lnoci/instant-client.html