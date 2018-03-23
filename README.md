# About RESTful
A simple webservice for FAB, unittest and functional tests included.
Source codes under 'restful directory', be orgnized as 2 files, restful_server.py and restful_client.py.

# Python version
First things first: Spyne is known to fully work on Python versions 3.3 and up. 

# Libraries
Additionally the following software packages are needed for RESTful:
A Wsgi server of your choice is needed to wrap spyne.server.wsgi.WsgiApplication
lxml>=3.2.5 is needed for any xml-related protocol.
lxml>=3.4.1 is needed for any html-related protocol.
Twisted is needed for anything in spyne.server.twisted and spyne.client.twisted.

# Installing
Go to top directory, then simply run the script directly from the command line:
$ python setup.py install

# Running Tests
Go to 'restful' directory, then simply run the script directly from the command line:
$ python3 test_suite.py
