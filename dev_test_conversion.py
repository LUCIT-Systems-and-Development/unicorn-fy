#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: dev_test_conversion.py
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

data = '{"e":"listStatus","E":1606946194410,"s":"ETHUSDT","g":10717037,"c":"OCO","l":"ALL_DONE","L":"ALL_DONE",' \
       '"r":"NONE","C":"i8B7NXuB37QkJ2Vy8f5KHh","T":1606946194409,"O":[{"s":"ETHUSDT","i":2175939815,' \
       '"c":"electron_648187c31bda49b6a2e81d23ae0"},{"s":"ETHUSDT","i":2175939816,"c":"84wruoWCZdkBUqbqlKfpv6"}]}'
result = UnicornFy.binance_com_websocket(data)
print(f"result: {result}")
