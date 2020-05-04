#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: test_tickers.py
#
# Part of ‘UnicornFy’
# Project website: https://github.com/oliver-zehentleitner/unicorn_fy
# Documentation: https://oliver-zehentleitner.github.io/unicorn_fy
# PyPI: https://pypi.org/project/unicorn-fy
#
# Author: Oliver Zehentleitner
#         https://about.me/oliver-zehentleitner
#
# Copyright (c) 2019, Oliver Zehentleitner
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

from unicorn_binance_websocket_api.unicorn_binance_websocket_api_manager import BinanceWebSocketApiManager
from unicorn_fy.unicorn_fy import UnicornFy

binance_websocket_api_manager = BinanceWebSocketApiManager(exchange="binance.com")
binance_websocket_api_manager.create_stream(['miniTicker'], ['btcusdt', 'bnbbtc', 'ethbtc'])
binance_websocket_api_manager.create_stream(['!miniTicker'], ['arr'])
binance_websocket_api_manager.create_stream(['ticker'], ['btcusdt', 'bnbbtc', 'ethbtc'])
binance_websocket_api_manager.create_stream(['!ticker'], ['arr'])

while True:
    oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
    if oldest_stream_data_from_stream_buffer:
        oldest_stream_data_from_stream_buffer = UnicornFy.binance_com_websocket(oldest_stream_data_from_stream_buffer)
        print(oldest_stream_data_from_stream_buffer)
