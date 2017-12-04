import requests

import pycurl
from io import BytesIO

import pytest
import json
import pprint

from .base import BaseTests

class TestStringMethods(BaseTests):

    @pytest.mark.skip(reason="skip it for a moment")
    def test_send_requests(self):

        resp = requests.get(self.ticker_url + "BTC")

        assert resp.status_code == 200

        print(self.R)
        pprint.pprint(json.loads(resp.content))
        print(self.W)


    def test_send_pycurl(self):
        buffer = BytesIO()
        header_buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, self.ticker_url + "BTC")
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.HEADERFUNCTION, header_buffer.write)

        c.perform()
        c.close()

        body = buffer.getvalue()
        header = header_buffer.getvalue()
        status_code = header[9:12]


        #  TODO:  <26-11-17, Daniel> #
        # need decoration!!!!!
        # 데코레이션 하는게 나음
        print(self.R)
        pprint.pprint(json.loads(body))
        print(self.W)
        # pprint.pprint(json.loads(header))
        print(self.G)
        pprint.pprint(json.loads(status_code))
        print(self.W)
        assert status_code == b"200"

    def test_public_orderbook(self):
        # https://api.bithumb.com/public/orderbook/{currency}
        buffer = BytesIO()
        header_buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, self.orderbook_url + "BTC")
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.HEADERFUNCTION, header_buffer.write)

        c.perform()
        c.close()

        body = buffer.getvalue()
        header = header_buffer.getvalue()
        status_code = header[9:12]

        #  TODO:  <26-11-17, Daniel> #
        # need decoration!!!!!
        # 데코레이션 하는게 나음
        print(self.R)
        pprint.pprint(json.loads(body))
        print(self.W)
        # pprint.pprint(json.loads(header))
        print(self.G)
        pprint.pprint(json.loads(status_code))
        print(self.W)
        assert status_code == b"200"

    def test_recent_transactions(self):
        # https://api.bithumb.com/public/recent_transactions/{currency}
        buffer = BytesIO()
        header_buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, self.recent_transactions_url+ "BTC")
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.HEADERFUNCTION, header_buffer.write)

        c.perform()
        c.close()

        body = buffer.getvalue()
        header = header_buffer.getvalue()
        status_code = header[9:12]


        #  TODO:  <26-11-17, Daniel> #
        # need decoration!!!!!
        # 데코레이션 하는게 나음
        print(self.R)
        pprint.pprint(json.loads(body))
        print(self.W)
        # pprint.pprint(json.loads(header))
        print(self.G)
        pprint.pprint(json.loads(status_code))
        print(self.W)
        assert status_code == b"200"

    @pytest.mark.skip(reason="skip it for a moment")
    def test_os_env_test(self):
        assert self.private_key == ""

    def test_sum_test(self):
        assert 1 + 1 == 2, ""
