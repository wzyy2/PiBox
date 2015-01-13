#! /bin/sh
umask 077
openssl req  -config "make_certificate.cfg" -keyout "webshell.pem" -newkey rsa -nodes -x509 -days 365 -out "webshell.pem"
