import pycurl
from io import BytesIO

import pytest

"""
Request
Parameter Name	Data Type	Description
apiKey	String	apiKey
secretKey	String	scretKey
order_id	String	판/구매 주문 등록된 주문번호
type	String	거래유형(bid : 구매, ask : 판매)
count	Int	Value : 1 ~1000 (default : 100)
after	Int	YYYY-MM-DD hh:mm:ss 의 UNIX Timestamp
(2014-11-28 16:40:01 = 1417160401000)
currency	String	BTC, ETH, DASH, LTC, ETC, XRP, BCH, XMR, ZEC, QTUM, BTG, EOS (기본값: BTC)


Response
status	결과 상태 코드 (정상 : 0000, 정상이외 코드는 에러 코드 참조)
order_currency	주문 화폐단위
order_date	주문일시 Timestamp
payment_currency	결제 화폐단위
type	주문요청 구분 (bid : 구매, ask : 판매)
status	주문상태(placed : 거래 진행 중)
units	거래요청 Currency (BTC, ETH, DASH, LTC, ETC, XRP, BCH, XMR, ZEC, QTUM, BTG, EOS)
units_remaining	주문 체결 잔액
price	1Currency당 거래금액 (BTC, ETH, DASH, LTC, ETC, XRP, BCH, XMR, ZEC, QTUM, BTG, EOS)
fee	거래 수수료
total	거래체결 완료 총 거래금액, 완료상태가 아닌 경우 NULL
date_completed	거래체결 완료일시 Timestamp, 완료상태가 아닌 경우 NULL
"""


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
            "count": 100,
            "searchGb": 0,
            "currency": "XRP"
        };
        resp = self.api.xcoinApiCall("/info/user_transactions", rgParams)
        assert resp["status"] == "0000"

        print(resp)

    @pytest.mark.skip(reason="skip it for a moment")
    def test_info_orders(self):
        # 현재 내가 거래중인 Currency를 보여주는데, Param 보내줘야합니다.
        # * {currency} = BTC, ETH, DASH, LTC, ETC, XRP, BCH, XMR, ZEC, QTUM, BTG, EOS (기본값: BTC), ALL(전체)
        """
        status	결과 상태 코드 (정상 : 0000, 정상이외 코드는 에러 코드 참조)
        order_currency	주문 화폐단위
        order_date	주문일시 Timestamp
        payment_currency	결제 화폐단위
        type	주문요청 구분 (bid : 구매, ask : 판매)
        status	주문상태(placed : 거래 진행 중)
        units	거래요청 Currency (BTC, ETH, DASH, LTC, ETC, XRP, BCH, XMR, ZEC, QTUM, BTG, EOS)
        units_remaining	주문 체결 잔액
        price	1Currency당 거래금액 (BTC, ETH, DASH, LTC, ETC, XRP, BCH, XMR, ZEC, QTUM, BTG, EOS)
        fee	거래 수수료
        total	거래체결 완료 총 거래금액, 완료상태가 아닌 경우 NULL
        date_completed	거래체결 완료일시 Timestamp, 완료상태가 아닌 경우 NULL
        """

        rgParams = {
            "type": "bid",
            "currency": "XRP"
        };
        resp = self.api.xcoinApiCall("/info/orders", rgParams)

        assert resp["status"] == "0000"
        print(resp)
