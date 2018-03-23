#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

suite  = unittest.TestLoader().discover("tests")
unittest.TextTestRunner(verbosity = 2).run(suite)
