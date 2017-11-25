import requests

import pycurl
from io import BytesIO

import pytest
import json
import pprint

from base import BaseTests

class TestStringMethods(BaseTests):

    @pytest.mark.skip(reason="skip it for a moment")
    def test_send_requests(self):

        resp = requests.get(self.info + "ALL")

        assert resp.status_code == 200

        print(self.R)
        pprint.pprint(json.loads(resp.content))
        print(self.W)


    def test_send_pycurl(self):
        buffer = BytesIO()
        header_buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, self.info + "BTC")
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.HEADERFUNCTION, header_buffer.write)

        c.perform()
        c.close()

        body = buffer.getvalue()
        header = header_buffer.getvalue()
        status_code = header[9:12]


        #  TODO:  <26-11-17, Daniel> #
        # print 하는 함수를 내가 데코레이팅하는 것이나을 듯..
        print(self.R)
        pprint.pprint(json.loads(body))
        print(self.W)
        # pprint.pprint(json.loads(header))
        print(self.G)
        pprint.pprint(json.loads(status_code))
        print(self.W)
        assert status_code == b"200"

