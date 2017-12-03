import unittest
import requests

import json
import pprint

import os

class BaseTests(unittest.TestCase):

    def setUp(self):
        self.private_key = os.getenv("PRIVATE_KEY")
        self.ticker_url = "https://api.bithumb.com/public/ticker/"
        self.orderbook_url = "https://api.bithumb.com/public/orderbook/"
        self.recent_transactions_url = "https://api.bithumb.com/public/recent_transactions/"

        self.W  = '\033[0m'  # white (normal)
        self.R  = '\033[31m' # red
        self.G  = '\033[32m' # green
        self.O  = '\033[33m' # orange
        self.B  = '\033[34m' # blue
        self.P  = '\033[35m' # purple

    def tearDown(self):
        pass
