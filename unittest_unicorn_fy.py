#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: unittest_unicorn_fy.py
#
# Part of ‘UnicornFy’
# Project website: https://github.com/oliver-zehentleitner/unicorn_fy
# Documentation: https://oliver-zehentleitner.github.io/unicorn_fy
# PyPI: https://pypi.org/project/unicorn-fy
#
# Author: Oliver Zehentleitner
#         https://about.me/oliver-zehentleitner
#
# Copyright (c) 2019-2020, Oliver Zehentleitner
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from unicorn_fy.unicorn_fy import UnicornFy
import logging
import unittest
import os

BINANCE_COM_API_KEY = ""
BINANCE_COM_API_SECRET = ""

# https://docs.python.org/3/library/logging.html#logging-levels
logging.basicConfig(level=logging.DEBUG,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")


class TestUnicornFy(unittest.TestCase):

    def setUp(self):
        self.unicorn_fy = UnicornFy()
        self.unicorn_fy_version = str(self.unicorn_fy.get_version())

    def test_aggTrade(self):
        data = '{"stream":"btcusdt@aggTrade","data":{"e":"aggTrade","E":1592584651517,"s":"BTCUSDT","a":315753210,"p":"9319.00000000","q":"0.01864900","f":343675554,"l":343675554,"T":1592584651516,"m":true,"M":true}}'
        asserted_result = "{'stream_type': 'btcusdt@aggTrade', 'event_type': 'aggTrade', 'event_time': 1592584651517, 'symbol': 'BTCUSDT', 'aggregate_trade_id': 315753210, 'price': '9319.00000000', 'quantity': '0.01864900', 'first_trade_id': 343675554, 'last_trade_id': 343675554, 'trade_time': 1592584651516, 'is_market_maker': True, 'ignore': True, 'unicorn_fied': ['binance.com', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_websocket(data)), asserted_result)

    def tearDown(self):
        del self.unicorn_fy


if __name__ == '__main__':
    unittest.main()
