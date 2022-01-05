Portifolio:
SMALL 3.

lb - HPROXY
./configlb

web1 - httpd
web2 - httpd
webdev - httpd table prefix: _webdev

./www
db - MYSQL
./dbconfig
app - ubuntu

networks:
skynet-fe
skynet-be

volume-web
volume-webdev
volume-db ./
volume lb ./lb

#APP
Pega dados da API clima e tempo, a cada 1 minuto e insere no banco.
API clima tempo:
----
Stack:
