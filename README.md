# project_bs
# 프로젝트 빗썸
## project_bs(bithumb)


# bithumb public API 
https://www.bithumb.com/u1/US127

```sh

GET:
# request
https://api.bithumb.com/public/ticker/{currency}
# * {currency} = BTC, ETH, DASH, LTC, ETC, XRP, BCH, XMR, ZEC, QTUM (기본값: BTC), ALL(전체)



# response
# HTTP_STATUS_200
{
    "status": "0000",
    "data": {
        "opening_price" : "504000",
        "closing_price" : "505000",
        "min_price"     : "504000",
        "max_price"     : "516000",
        "average_price" : "509533.3333",
        "units_traded"  : "14.71960286",
        "volume_1day"   : "14.71960286",
        "volume_7day"   : "15.81960286",
        "buy_price"     : "505000",
        "sell_price"    : "504000",
        "date"          : 1417141032622
    }
}

```


# Quick Start
```

# install dependencis
# 의존 패키지들 설치 
pip install -r developments.txt

# run test
# 테스트 실행
pytest -s -v 
# 또는 or 
./pytest.sh

```
