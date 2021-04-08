#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: dev_test_conversion.py
#
# Part of ‘UnicornFy’
# Project website: https://github.com/oliver-zehentleitner/unicorn-fy
# Documentation: https://oliver-zehentleitner.github.io/unicorn-fy
# PyPI: https://pypi.org/project/unicorn-fy
#
# Author: Oliver Zehentleitner
#         https://about.me/oliver-zehentleitner
#
# Copyright (c) 2019-2021, Oliver Zehentleitner
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

data = '{"e":"ORDER_TRADE_UPDATE","T":1617859867769,"E":1617859867772,"o":{"s":"SANDUSDT","c":"electron_6LyJZ9KPgmRbhKfFamx3","S":"BUY","o":"LIMIT","f":"GTC","q":"1000","p":"0.63428","ap":"0","sp":"0","x":"NEW","X":"NEW","i":315803079,"l":"0","z":"0","L":"0","T":1617859867769,"t":0,"b":"1262.16000","a":"0","m":false,"R":false,"wt":"CONTRACT_PRICE","ot":"LIMIT","ps":"LONG","cp":false,"rp":"0","pP":false,"si":0,"ss":0}}'
result = UnicornFy.binance_futures_websocket(data)
print(f"result: {result}")
