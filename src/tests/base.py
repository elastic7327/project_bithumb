import unittest
import requests

import json
import pprint

import os

class BaseTests(unittest.TestCase):

    def setUp(self):

        # 개인키
        self.secret_key = os.getenv("SECRET_KEY")
        # 커넥션키
        self.connect_key = os.getenv("CONNECTION_KEY")

        # bithumb 거래소 마지막 거래 정보
        self.ticker_url = "https://api.bithumb.com/public/ticker/"

        # bithumb 거래소 판/구매 등록 대기 또는 거래 중 내역 정보
        self.orderbook_url = "https://api.bithumb.com/public/orderbook/"

        # bithumb 거래소 거래 체결 완료 내역
        self.recent_transactions_url = "https://api.bithumb.com/public/recent_transactions/"

        # bithumb 거래소 회원 정보
        self.account_info_pri = "https://api.bithumb.com/info/account"

        # bithumb 거래소 회원 지갑 정보
        self.balance_pri = "https://api.bithumb.com/info/balance"

        # bithumb 거래소 회원 입금 주소
        self.wallet_address_pri = "https://api.bithumb.com/info/wallet_address"

        # 회원 마지막 거래 정보
        self.last_info_ticker_pri = "https://api.bithumb.com/info/ticker"

        # 판/구매 거래 주문 등록 또는 진행 중인 거래
        self.info_orders_pri = "https://api.bithumb.com/info/orders"

        self.W  = '\033[0m'  # white (normal)
        self.R  = '\033[31m' # red
        self.G  = '\033[32m' # green
        self.O  = '\033[33m' # orange
        self.B  = '\033[34m' # blue
        self.P  = '\033[35m' # purple

    def tearDown(self):
        pass
