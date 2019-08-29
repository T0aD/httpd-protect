# httpd-protect.py

This is a simple code for a simple but yet very interesting need:
- protect a single or a group of port(s) from outside access
- allow it to a set of given remote addresses
- whitelist those addresses by a simple auth mechanism (Basic HTTP auth)
- work even behind a docker-proxy (using header X-Forwarded-For)





