# RESTful
webservice for FAB
# About
Spyne aims to save the protocol implementers the hassle of implementing their own remote procedure call api and the application programmers the hassle of jumping through hoops just to expose their services using multiple protocols and transports.

You can download Spyne releases from Github or PyPi.

# Requirements
Spyne source distribution is a collection of highly decoupled components, which makes it a bit difficult to put a simple list of requirements, as literally everything except pytz is optional.

# Python version
First things first: Spyne is known to fully work on Python versions 3.3 and up. 

# Libraries
Additionally the following software packages are needed for various subsystems of Spyne:

A Wsgi server of your choice is needed to wrap spyne.server.wsgi.WsgiApplication
lxml>=3.2.5 is needed for any xml-related protocol.
lxml>=3.4.1 is needed for any html-related protocol.
SQLAlchemy is needed for spyne.model.complex.TTableModel.
pyzmq is needed for spyne.client.zeromq.ZeroMQClient and spyne.server.zeromq.ZeroMQServer.
Werkzeug is needed for using spyne.protocol.http.HttpRpc under a wsgi transport.
PyParsing is needed for using HttpPattern's with spyne.protocol.http.HttpRpc.
Twisted is needed for anything in spyne.server.twisted and spyne.client.twisted.
Django (tested with 1.8 and up) is needed for anything in spyne.server.django.
Pyramid is needed for spyne.server.pyramid.PyramidApplication.
msgpack-python is needed for spyne.protocol.msgpack.
PyYaml is needed for spyne.protocol.yaml.
simplejson is used when found for spyne.protocol.json.
You are advised to add these as requirements to your own projects, as these are only optional dependencies of Spyne, thus not handled in its setup script.

# Installing

# Getting Support

# Contributing

# Acknowledgments
