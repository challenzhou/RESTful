#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Application is the glue between one or more service definitions, interface and protocol choices.
from spyne import Application
# @rpc decorator exposes methods as remote procedure calls
# and declares the data types it accepts and returns
from spyne import rpc
# spyne.service.ServiceBase is the base class for all service definitions.
from spyne import ServiceBase
# The names of the needed types for implementing this service should be self-explanatory.
from spyne import Iterable, Integer, Unicode

from spyne.protocol.soap import Soap11
# Our server is going to use HTTP as transport, It’s going to wrap the Application instance.
from spyne.server.wsgi import WsgiApplication

import sys


class RestfulService(ServiceBase):
    @rpc(Integer, _returns=Iterable(Integer))
    def fibonacci(self, count):
        n, a, b = 0, 0, 1
        res = []
        while n < count:
            res.append(a)
            a, b = b, a + b
            n = n + 1
        return res

# step2: Glue the service definition, input and output protocols
soap_app = Application([RestfulService], 'RESTFUL_SERVICE',
                       in_protocol=Soap11(validator='lxml'),
                       out_protocol=Soap11())

# step3: Wrap the Spyne application with its wsgi wrapper
wsgi_app = WsgiApplication(soap_app)

if __name__ == '__main__':

    try:
        import logging
        from wsgiref.simple_server import make_server
        # configure the python logger to show debugging output
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

        logging.info("listening to http://127.0.0.1:8000")
        logging.info("wsdl is at: http://localhost:8000/?wsdl")

        # step4:Deploying the service using Soap via Wsgi
        # register the WSGI application as the handler to the wsgi server, and run the http server
        server = make_server('localhost', 8000, wsgi_app)
        sys.exit(server.serve_forever())

    except ServerError:
        # need to figure out error details
        logger.exception('server exception')
