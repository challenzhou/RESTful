# -*- coding: utf-8 -*-

import unittest
from restful_server import *


class TestServerFunc(unittest.TestCase):
    def setUp(self):
        self.tclass = RestfulService()

    def tearDown(self):
        pass

    """Test restful_server.py"""
    def test_fibonacci_count_positive(self):
        """Test method finomacci(count)"""
        for i in range(10):
            res = self.tclass.fibonacci(self.tclass, i)
            self.assertEqual(i, len(res))

    def test_fibonacci_count_negative(self):
        """Test method finomacci(count)"""
        for i in range(-10, -1):
            res = self.tclass.fibonacci(self.tclass, i)
            self.assertEqual(0, len(res))

    def test_fibonacci_data(self):
        """Test method finomacci(count)"""
        res = self.tclass.fibonacci(self.tclass, 1)
        self.assertEqual([0], res)
        res = self.tclass.fibonacci(self.tclass, 2)
        self.assertEqual([0, 1], res)
        res = self.tclass.fibonacci(self.tclass, 3)
        self.assertEqual([0, 1, 1], res)
        res = self.tclass.fibonacci(self.tclass, 5)
        self.assertEqual([0, 1, 1, 2, 3], res)
        res = self.tclass.fibonacci(self.tclass, 8)
        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13], res)

if __name__ == '__main__':
    unittest.main()