import pycurl
from io import BytesIO

import pytest

# from .xcoin_api_client import XCoinAPI


from .base import BaseTests

class TestPrivateApi(BaseTests):

    @pytest.mark.skip(reason="skip it for a moment")
    def test_account_info_requests(self):

        rgParams = {
                # "currency": "BTC"
        };
        resp = self.api.xcoinApiCall("/info/account", rgParams)
        assert resp["status"] == "0000"

        print(resp)

    @pytest.mark.skip(reason="skip it for a moment")
    def test_balance_check(self):
        rgParams = {
            "currency" : "DASH" # BTC, XRP etc etc
        };
        resp = self.api.xcoinApiCall("/info/balance", rgParams)
        assert resp["status"] == "0000"

        print(resp)

    @pytest.mark.skip(reason="skip it for a moment")
    def test_wallet_address_check(self):
        rgParams = {
            "currency" : "DASH" # BTC, XRP etc etc
        };
        resp = self.api.xcoinApiCall("/info/wallet_address", rgParams)
        assert resp["status"] == "0000"

        print(resp)

    @pytest.mark.skip(reason="skip it for a moment")
    def test_latest_order_info_ticker(self):
        rgParams = {
            "payment_currency" : "KRW", # BTC, XRP etc etc
            "order_currency": "BTC"
        };
        resp = self.api.xcoinApiCall("/info/wallet_address", rgParams)
        assert resp["status"] == "0000"

        print(resp)

    @pytest.mark.skip(reason="skip it for a moment")
    def test_order_ticker(self):
        pass

    @pytest.mark.skip(reason="skip it for a moment")
    def test_user_transactions(self):
        rgParams = {
            "offset" : 1,
            "count": 1,
            "searchGb": 1,
            "currency": "QTUM"
        };
        resp = self.api.xcoinApiCall("/info/user_transactions", rgParams)
        assert resp["status"] == "0000"

        print(resp)
