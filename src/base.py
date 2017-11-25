import unittest
import requests

import json
import pprint

class BaseTests(unittest.TestCase):

    def setUp(self):
        self.info = "https://api.bithumb.com/public/ticker/"

        self.W  = '\033[0m'  # white (normal)
        self.R  = '\033[31m' # red
        self.G  = '\033[32m' # green
        self.O  = '\033[33m' # orange
        self.B  = '\033[34m' # blue
        self.P  = '\033[35m' # purple

    def tearDown(self):
        pass
