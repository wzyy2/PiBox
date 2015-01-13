WebShell
========
[WebShell](https://github.com/xypiie/WebShell) is a web-based shell.

It runs on any browser capable of JavaScript and AJAX. You can use it from any
computer or iPhone/smartphone.

You'll get full access to a shell on the server, so you can use it e.g. to
connect to other computers using ssh or use an terminal based chat client.

The server is written in Python and is very easy to set up on Linux, Mac OS X,
BSD, Solaris, and any Unix that runs python 2.7.

WebShell is based on Ajaxterm.

Author
------
Peter Feuerer <peter[at]piie.net>

Installation
------------
Ensure python 2.7.X and OpenSSL are installed on your system. You will also
have to install the pyOpenSSL python extensions to OpenSSL.

Get the WebShell code:

	git clone https://github.com/xypiie/WebShell

Next, you need to generate a server certificate. From the WebShell
directory.  Therefor you need to open make_certificate.cfg in your favorite
editor and replace following variables by real content:
 * __MY_PASS__		<- put some secret password here
 * __FQDN__		<- replace it by the hostname you are going to use in
			   browser to access the page, e.g. my_host.com if you
			   want to address it on https://my_host.com:8022
 * __CHALLENGE_PASS__ 	<- some other secret password

Then enter this command to quickly generate a certificate:

	./make_certificate.sh

Now issue this command to run the WebShell server:

	./webshell.py

To make sure that everything went well, go to this URL in your
browser:

	https://127.0.0.1:8022

Voila, enjoy WebShell.

Features
--------
 * VT100, ECMA-48 terminal emulation
 * Integrated secure http server
 * UTF-8, with chinese/japanese wide glyph support
 * Virtual keyboard for Smartphone users
 * Changeable appearance
 * Compliant with vttest

Security
--------
WebShell communications are as secure as a regular secure shell, as
both ssh and WebShell are on top of the SSL/TLS layer.

The code has been tested against buffer overflow and denial of
service. If you find any problem, please report it on the webpage.

Origin
------
It is a fork of [WebShell](https://code.google.com/p/web-shell/) created by
 * Marc S. Ressl
 * Aleksander Adamowski

Thanks for your great work!
