import pycurl
from io import BytesIO

import pytest

from .xcoin_api_client import XCoinAPI


from .base import BaseTests

class TestPrivateApi(BaseTests):
    def test_account_info_requests(self):
        api = XCoinAPI(self.connect_key, self.secret_key)

        rgParams = {
            "order_currency" : "BTC",
            "payment_currency" : "KRW"
        };
        resp = api.xcoinApiCall("/info/account", rgParams)
        assert resp["status"] == "0000"

        print(resp)

