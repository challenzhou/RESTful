#!/usr/bin/env python
# -*- coding: utf-8 -*-

from suds.client import Client

wsdl_url = "http://localhost:8000/?wsdl"

def fibonacci_test(url, count):
    client = Client(url)
    return client.service.fibonacci(count)

if __name__ == '__main__':

    for i in range(-5, 20):
        res = fibonacci_test(wsdl_url, i)
        if res:
            print(res)
        else:
            print('no response with i(%d)' % i)
