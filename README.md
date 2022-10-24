# Serviço Interno de Resolução de Nomes

O sistema da NoHarm.ai não armazena na base de dados os nomes dos pacientes por conta da privacidade dos dados e pela Lei Geral de Proteção de Dados (LGPD). Para que a NoHarm.ai resolva os nomes dos paciente é necessário que um serviço seja exposto na intranet do hospital. O serviço recebe o número do paciente e retorna o nome do paciente. Esse serviço deve estar disponível somente dentro da intranet do hospital. A NoHarm.ai resolve os nomes do lado do cliente (client-side). O parâmetro idPatient é o identificador único da Pessoa.

O serviço deve receber o número do paciente por queryString. Esse serviço obrigatoriamente deve ser exposto através do protocolo SSL. Exemplo:
- https://intranet.hospital.com/resolveNome/{idPatient}
- https://intranet.hospital.com/resolveNome?idPatient={idPatient}

O serviço deve devolver o nome através de um documento JSON. Exemplo:
```
{ status: "success" , idPatient: 12345 , name: "João da Silva e Santos" }
```

Lembre-se adicionar no cabeçalho a liberação do CORS:
```
Access-Control-Allow-Origin: *
```

### 1. Run Docker

```
git clone https://github.com/noharm-ai/getname-api

cd getname-api

docker build -t getname . #build

docker run -p 443:443 getname #test

docker run -d --name mygetname -p 443:443 getname #deamon
```

### 1.1 Test

```
$ curl https://nomedocliente.getname.noharm.ai/patient-name/12345
```

### 2.1 Development

```
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

### 2.2 Install Oracle Cli

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

### 2.3 Let's Encrypt Certificate

```
sudo apt install certbot python3-certbot-nginx
sudo certbot run -a manual -i nginx -d *.domain.com
sudo certbot renew
```

### 2.4 Partial Update
```
git pull
git checkout origin/master Dockerfile tmp.conf
```
