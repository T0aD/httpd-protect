# httpd-protect.py

This is a simple code for a simple but yet very interesting need:
- protect a single or a group of port(s) from outside access
- allow it to a set of given remote addresses
- whitelist those addresses by a simple auth mechanism (Basic HTTP auth)
- work even behind a docker-proxy (using header X-Forwarded-For)

## Usage

``` shell

rulio@ghost:~/walky/httpd-protect$ ./httpd.py -h
usage: httpd.py [-h] [--port PORT] [--username USERNAME] [--password PASSWORD]
                [--realm REALM]
                [--protected-port [PROTECTED_PORT [PROTECTED_PORT ...]]]
                [--chain-name CHAIN_NAME] [--allow [ALLOW [ALLOW ...]]]

optional arguments:
  -h, --help            show this help message and exit

Server:
  --port PORT, -p PORT  port to bind httpd server to (default: 3003)

Basic auth:
  --username USERNAME   username used to whitelist (default: admin)
  --password PASSWORD   password to whitelist (default: adminpwd)
  --realm REALM         name of the realm to display (default: httpd-protect)

Iptables:
  --protected-port [PROTECTED_PORT [PROTECTED_PORT ...]]
                        port to protect (default: [9200, 9300])
  --chain-name CHAIN_NAME
                        default name of the chain to use to protect targetted
                        ports (default: httpd-protected)
  --allow [ALLOW [ALLOW ...]]
                        list of addresses to whitelist from the start
                        (default: ['172/8'])

```




