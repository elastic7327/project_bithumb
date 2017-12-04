
import requests

import pycurl
from io import BytesIO

import pytest
import json
import pprint

from .base import BaseTests

class TestPrivateApi(BaseTests):
    def test_account_info_requests(self):

        currency = "BTC"

        data = {
            "apiKey": self.connect_key,
            "secretKey": self.secret_key,
            "currency": currency
        }

        resp = requests.post(self.account_info_pri, data=data)

        print (resp.content)

        assert resp.status_code == 200

        print(self.R)
        pprint.pprint(json.loads(resp.content))
        print (resp.content)
        print(self.W)

