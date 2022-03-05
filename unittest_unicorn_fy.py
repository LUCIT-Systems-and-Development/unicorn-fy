#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# File: unittest_unicorn_fy.py
#
# Part of ‘UnicornFy’
# Project website: https://www.lucit.tech/unicorn-fy.html
# Github: https://github.com/LUCIT-Systems-and-Development/unicorn-fy
# Documentation: https://unicorn-fy.docs.lucit.tech/
# PyPI: https://pypi.org/project/unicorn-fy
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2019-2022, LUCIT Systems and Development (https://www.lucit.tech) and Oliver Zehentleitner
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

import unicorn_binance_websocket_api
import unicorn_binance_rest_api
from unicorn_fy.unicorn_fy import UnicornFy
import logging
import unittest
import os
import time
import threading


# Todo: Add stream_everything with rest

# https://docs.python.org/3/library/logging.html#logging-levels
logging.basicConfig(level=logging.ERROR,
                    filename=os.path.basename(__file__) + '.log',
                    format="{asctime} [{levelname:8}] {process} {thread} {module}: {message}",
                    style="{")

print("Starting unittests")


def print_stream_data_from_stream_buffer(binance_websocket_api_manager):
    while True:
        if binance_websocket_api_manager.is_manager_stopping():
            exit(0)
        oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
        if oldest_stream_data_from_stream_buffer is not False:
            unicorn_fied_data = UnicornFy.binance_com_websocket(oldest_stream_data_from_stream_buffer)
            #print(str(unicorn_fied_data))
        else:
            time.sleep(0.01)


def print_stream_data_from_stream_buffer_futures(binance_websocket_api_manager):
    while True:
        if binance_websocket_api_manager.is_manager_stopping():
            exit(0)
        oldest_stream_data_from_stream_buffer = binance_websocket_api_manager.pop_stream_data_from_stream_buffer()
        if oldest_stream_data_from_stream_buffer is not False:
            unicorn_fied_data = UnicornFy.binance_com_futures_websocket(oldest_stream_data_from_stream_buffer)
            #print(str(unicorn_fied_data))
        else:
            time.sleep(0.01)


class TestBinanceGeneric(unittest.TestCase):
    def setUp(self):
        self.unicorn_fy = UnicornFy()
        self.unicorn_fy_version = str(self.unicorn_fy.get_version())
        self.unicorn_fy.get_latest_release_info()
        self.unicorn_fy.get_latest_version()

    def test_set_to_false_if_not_exist(self):
        value = {'key': '',
                 'blub': 2}
        self.assertEqual(str(self.unicorn_fy.set_to_false_if_not_exist(value, "invalid")),
                         "{'key': '', 'blub': 2, 'invalid': False}")

    def test_is_json(self):
        self.assertFalse(self.unicorn_fy.is_json(False))

    def test_result(self):
        data = '{"result":null,"id":2}'
        asserted_result = "{'result': None, 'id': 2, 'unicorn_fied': ['binance.com', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_websocket(data)), asserted_result)

    def test_error(self):
        data = '{"error":"blahblah"}'
        asserted_result = "{'error': 'blahblah', 'unicorn_fied': ['binance.com', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_websocket(data)), asserted_result)

    def test_template(self):
        data = ''
        asserted_result = ""
        self.assertEqual(str(self.unicorn_fy.binance_com_margin_websocket(data)), asserted_result)

    def tearDown(self):
        del self.unicorn_fy


class TestBinanceComWebsocket(unittest.TestCase):
    def setUp(self):
        self.unicorn_fy = UnicornFy()
        self.unicorn_fy_version = str(self.unicorn_fy.get_version())
        data = '{"stream":"btcusdt@aggTrade","data":{"e":"aggTrade","E":1592584651517,"s":"BTCUSDT","a":315753210,"p":"9319.00000000","q":"0.01864900","f":343675554,"l":343675554,"T":1592584651516,"m":true,"M":true}}'
        self.unicorn_fy.binance_websocket(data, show_deprecated_warning=True)

    def test_aggTrade_single(self):
        data = '{"stream":"btcusdt@aggTrade","data":{"e":"aggTrade","E":1592584651517,"s":"BTCUSDT","a":315753210,"p":"9319.00000000","q":"0.01864900","f":343675554,"l":343675554,"T":1592584651516,"m":true,"M":true}}'
        asserted_result = "{'stream_type': 'btcusdt@aggTrade', 'event_type': 'aggTrade', 'event_time': 1592584651517, 'symbol': 'BTCUSDT', 'aggregate_trade_id': 315753210, 'price': '9319.00000000', 'quantity': '0.01864900', 'first_trade_id': 343675554, 'last_trade_id': 343675554, 'trade_time': 1592584651516, 'is_market_maker': True, 'ignore': True, 'unicorn_fied': ['binance.com', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_websocket(data)), asserted_result)

    def test_trade_single(self):
        data = '{"stream":"btcusdt@trade","data":{"e":"trade","E":1592591955766,"s":"BTCUSDT","t":343719861,"p":"9302.00000000","q":"0.00101900","b":2517144287,"a":2517144235,"T":1592591955765,"m":false,"M":true}}'
        asserted_result = "{'stream_type': 'btcusdt@trade', 'event_type': 'trade', 'event_time': 1592591955766, 'symbol': 'BTCUSDT', 'trade_id': 343719861, 'price': '9302.00000000', 'quantity': '0.00101900', 'buyer_order_id': 2517144287, 'seller_order_id': 2517144235, 'trade_time': 1592591955765, 'is_market_maker': False, 'ignore': True, 'unicorn_fied': ['binance.com', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_websocket(data)), asserted_result)

    def test_ticker_single(self):
        data = '{"stream":"btcusdt@ticker","data":{"e":"24hrTicker","E":1592593727005,"s":"BTCUSDT","p":"-65.00000000","P":"-0.693","w":"9343.29777965","x":"9383.27000000","c":"9318.48000000","Q":"0.00250000","b":"9318.18000000","B":"0.32000000","a":"9318.47000000","A":"0.35414300","o":"9383.48000000","h":"9438.30000000","l":"9215.79000000","v":"48745.36667100","q":"455442476.18534620","O":1592507327001,"C":1592593727001,"F":343178738,"L":343729077,"n":550340}}'
        asserted_result = "{'stream_type': 'btcusdt@ticker', 'event_type': '24hrTicker', 'data': [{'stream_type': 'btcusdt@ticker', 'event_type': '24hrTicker', 'event_time': 1592593727005, 'symbol': 'BTCUSDT', 'price_change': '-65.00000000', 'price_change_percent': '-0.693', 'weighted_average_price': '9343.29777965', 'trade_before_24h_window': '9383.27000000', 'last_price': '9318.48000000', 'last_quantity': '0.00250000', 'best_bid_price': '9318.18000000', 'best_bid_quantity': '0.32000000', 'best_ask_price': '9318.47000000', 'best_ask_quantity': '0.35414300', 'open_price': '9383.48000000', 'high_price': '9438.30000000', 'low_price': '9215.79000000', 'total_traded_base_asset_volume': '48745.36667100', 'total_traded_quote_asset_volume': '455442476.18534620', 'statistics_open_time': 1592507327001, 'statistics_close_time': 1592593727001, 'first_trade_id': 343178738, 'last_trade_id': 343729077, 'total_nr_of_trades': 550340}], 'unicorn_fied': ['binance.com', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_websocket(data)), asserted_result)

    def test_miniTicker_arr(self):
        data = '[{"e":"24hrMiniTicker","E":1592594715455,"s":"ETHBTC","c":"0.02456700","o":"0.02459800","h":"0.02470900","l":"0.02438100","v":"163116.18600000","q":"4006.04936991"},{"e":"24hrMiniTicker","E":1592594715775,"s":"BTCUSDT","c":"9342.70000000","o":"9393.74000000","h":"9438.30000000","l":"9215.79000000","v":"47798.03832300","q":"446546826.58722200"},{"e":"24hrMiniTicker","E":1592594715488,"s":"ETHUSDT","c":"229.47000000","o":"231.06000000","h":"232.69000000","l":"226.74000000","v":"439855.40218000","q":"100960868.33504020"},{"e":"24hrMiniTicker","E":1592594715714,"s":"LINKBTC","c":"0.00043725","o":"0.00044065","h":"0.00044673","l":"0.00043490","v":"1034299.00000000","q":"456.44873499"},{"e":"24hrMiniTicker","E":1592594715746,"s":"LINKETH","c":"0.01781759","o":"0.01789017","h":"0.01817306","l":"0.01770212","v":"75699.00000000","q":"1359.70614144"},{"e":"24hrMiniTicker","E":1592594715757,"s":"ETCBTC","c":"0.00068510","o":"0.00065590","h":"0.00068720","l":"0.00065400","v":"283704.17000000","q":"190.31163530"},{"e":"24hrMiniTicker","E":1592594715436,"s":"TRXETH","c":"0.00006977","o":"0.00006925","h":"0.00006999","l":"0.00006898","v":"57356284.00000000","q":"3980.89377161"},{"e":"24hrMiniTicker","E":1592594715681,"s":"TNBBTC","c":"0.00000031","o":"0.00000029","h":"0.00000031","l":"0.00000028","v":"334919689.00000000","q":"97.62568721"},{"e":"24hrMiniTicker","E":1592594715454,"s":"ELFBTC","c":"0.00001121","o":"0.00001105","h":"0.00001134","l":"0.00001052","v":"7105620.00000000","q":"78.17667453"},{"e":"24hrMiniTicker","E":1592594715442,"s":"ELFETH","c":"0.00045625","o":"0.00045000","h":"0.00046193","l":"0.00042902","v":"261232.00000000","q":"116.09339754"},{"e":"24hrMiniTicker","E":1592594715696,"s":"RLCBTC","c":"0.00006922","o":"0.00005916","h":"0.00007305","l":"0.00005752","v":"7289087.00000000","q":"493.31904576"},{"e":"24hrMiniTicker","E":1592594714915,"s":"ADAUSDT","c":"0.08013000","o":"0.08099000","h":"0.08239000","l":"0.07844000","v":"297708746.40000000","q":"23902853.53009500"},{"e":"24hrMiniTicker","E":1592594715812,"s":"DATABTC","c":"0.00000585","o":"0.00000584","h":"0.00000618","l":"0.00000570","v":"12724161.00000000","q":"75.51506149"},{"e":"24hrMiniTicker","E":1592594715768,"s":"ETCUSDT","c":"6.40130000","o":"6.16160000","h":"6.42130000","l":"6.09630000","v":"1368917.75000000","q":"8580762.83062200"},{"e":"24hrMiniTicker","E":1592594715388,"s":"FETUSDT","c":"0.03144000","o":"0.03100000","h":"0.03188000","l":"0.02923000","v":"225670248.30000000","q":"6911155.91613500"},{"e":"24hrMiniTicker","E":1592594714974,"s":"BATUSDT","c":"0.21920000","o":"0.21810000","h":"0.22300000","l":"0.21390000","v":"7422701.22000000","q":"1619349.76348900"},{"e":"24hrMiniTicker","E":1592594715293,"s":"IOSTUSDT","c":"0.00578900","o":"0.00568200","h":"0.00605200","l":"0.00557400","v":"1610340020.00000000","q":"9367137.54193700"},{"e":"24hrMiniTicker","E":1592594715370,"s":"ERDBTC","c":"0.00000057","o":"0.00000047","h":"0.00000059","l":"0.00000044","v":"2092244908.00000000","q":"1087.58437768"},{"e":"24hrMiniTicker","E":1592594715719,"s":"TOMOBNB","c":"0.02937000","o":"0.02784000","h":"0.02937000","l":"0.02705000","v":"98503.20000000","q":"2766.91140800"},{"e":"24hrMiniTicker","E":1592594715796,"s":"TOMOBTC","c":"0.00005045","o":"0.00004779","h":"0.00005048","l":"0.00004652","v":"2978511.00000000","q":"144.42861171"},{"e":"24hrMiniTicker","E":1592594715535,"s":"TOMOUSDT","c":"0.46920000","o":"0.44930000","h":"0.47170000","l":"0.43000000","v":"2175928.92000000","q":"983414.94253100"},{"e":"24hrMiniTicker","E":1592594715403,"s":"BEAMUSDT","c":"0.50340000","o":"0.49170000","h":"0.53000000","l":"0.48070000","v":"2266897.49000000","q":"1148328.48354700"},{"e":"24hrMiniTicker","E":1592594715042,"s":"VITEBTC","c":"0.00000190","o":"0.00000184","h":"0.00000195","l":"0.00000173","v":"35965553.00000000","q":"66.24169781"},{"e":"24hrMiniTicker","E":1592594715034,"s":"VITEUSDT","c":"0.01773000","o":"0.01730000","h":"0.01821000","l":"0.01606000","v":"15621038.00000000","q":"268307.71989000"},{"e":"24hrMiniTicker","E":1592594715251,"s":"MBLBNB","c":"0.00011700","o":"0.00011350","h":"0.00011880","l":"0.00010980","v":"83375259.00000000","q":"9505.73917390"},{"e":"24hrMiniTicker","E":1592594715431,"s":"KNCUSDT","c":"1.19900000","o":"1.15600000","h":"1.22400000","l":"1.14000000","v":"939178.01300000","q":"1109490.22233400"}]'
        asserted_result = "{'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'data': [{'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715455, 'symbol': 'ETHBTC', 'close_price': '0.02456700', 'open_price': '0.02459800', 'high_price': '0.02470900', 'low_price': '0.02438100', 'taker_by_base_asset_volume': '163116.18600000', 'taker_by_quote_asset_volume': '4006.04936991'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715775, 'symbol': 'BTCUSDT', 'close_price': '9342.70000000', 'open_price': '9393.74000000', 'high_price': '9438.30000000', 'low_price': '9215.79000000', 'taker_by_base_asset_volume': '47798.03832300', 'taker_by_quote_asset_volume': '446546826.58722200'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715488, 'symbol': 'ETHUSDT', 'close_price': '229.47000000', 'open_price': '231.06000000', 'high_price': '232.69000000', 'low_price': '226.74000000', 'taker_by_base_asset_volume': '439855.40218000', 'taker_by_quote_asset_volume': '100960868.33504020'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715714, 'symbol': 'LINKBTC', 'close_price': '0.00043725', 'open_price': '0.00044065', 'high_price': '0.00044673', 'low_price': '0.00043490', 'taker_by_base_asset_volume': '1034299.00000000', 'taker_by_quote_asset_volume': '456.44873499'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715746, 'symbol': 'LINKETH', 'close_price': '0.01781759', 'open_price': '0.01789017', 'high_price': '0.01817306', 'low_price': '0.01770212', 'taker_by_base_asset_volume': '75699.00000000', 'taker_by_quote_asset_volume': '1359.70614144'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715757, 'symbol': 'ETCBTC', 'close_price': '0.00068510', 'open_price': '0.00065590', 'high_price': '0.00068720', 'low_price': '0.00065400', 'taker_by_base_asset_volume': '283704.17000000', 'taker_by_quote_asset_volume': '190.31163530'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715436, 'symbol': 'TRXETH', 'close_price': '0.00006977', 'open_price': '0.00006925', 'high_price': '0.00006999', 'low_price': '0.00006898', 'taker_by_base_asset_volume': '57356284.00000000', 'taker_by_quote_asset_volume': '3980.89377161'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715681, 'symbol': 'TNBBTC', 'close_price': '0.00000031', 'open_price': '0.00000029', 'high_price': '0.00000031', 'low_price': '0.00000028', 'taker_by_base_asset_volume': '334919689.00000000', 'taker_by_quote_asset_volume': '97.62568721'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715454, 'symbol': 'ELFBTC', 'close_price': '0.00001121', 'open_price': '0.00001105', 'high_price': '0.00001134', 'low_price': '0.00001052', 'taker_by_base_asset_volume': '7105620.00000000', 'taker_by_quote_asset_volume': '78.17667453'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715442, 'symbol': 'ELFETH', 'close_price': '0.00045625', 'open_price': '0.00045000', 'high_price': '0.00046193', 'low_price': '0.00042902', 'taker_by_base_asset_volume': '261232.00000000', 'taker_by_quote_asset_volume': '116.09339754'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715696, 'symbol': 'RLCBTC', 'close_price': '0.00006922', 'open_price': '0.00005916', 'high_price': '0.00007305', 'low_price': '0.00005752', 'taker_by_base_asset_volume': '7289087.00000000', 'taker_by_quote_asset_volume': '493.31904576'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594714915, 'symbol': 'ADAUSDT', 'close_price': '0.08013000', 'open_price': '0.08099000', 'high_price': '0.08239000', 'low_price': '0.07844000', 'taker_by_base_asset_volume': '297708746.40000000', 'taker_by_quote_asset_volume': '23902853.53009500'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715812, 'symbol': 'DATABTC', 'close_price': '0.00000585', 'open_price': '0.00000584', 'high_price': '0.00000618', 'low_price': '0.00000570', 'taker_by_base_asset_volume': '12724161.00000000', 'taker_by_quote_asset_volume': '75.51506149'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715768, 'symbol': 'ETCUSDT', 'close_price': '6.40130000', 'open_price': '6.16160000', 'high_price': '6.42130000', 'low_price': '6.09630000', 'taker_by_base_asset_volume': '1368917.75000000', 'taker_by_quote_asset_volume': '8580762.83062200'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715388, 'symbol': 'FETUSDT', 'close_price': '0.03144000', 'open_price': '0.03100000', 'high_price': '0.03188000', 'low_price': '0.02923000', 'taker_by_base_asset_volume': '225670248.30000000', 'taker_by_quote_asset_volume': '6911155.91613500'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594714974, 'symbol': 'BATUSDT', 'close_price': '0.21920000', 'open_price': '0.21810000', 'high_price': '0.22300000', 'low_price': '0.21390000', 'taker_by_base_asset_volume': '7422701.22000000', 'taker_by_quote_asset_volume': '1619349.76348900'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715293, 'symbol': 'IOSTUSDT', 'close_price': '0.00578900', 'open_price': '0.00568200', 'high_price': '0.00605200', 'low_price': '0.00557400', 'taker_by_base_asset_volume': '1610340020.00000000', 'taker_by_quote_asset_volume': '9367137.54193700'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715370, 'symbol': 'ERDBTC', 'close_price': '0.00000057', 'open_price': '0.00000047', 'high_price': '0.00000059', 'low_price': '0.00000044', 'taker_by_base_asset_volume': '2092244908.00000000', 'taker_by_quote_asset_volume': '1087.58437768'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715719, 'symbol': 'TOMOBNB', 'close_price': '0.02937000', 'open_price': '0.02784000', 'high_price': '0.02937000', 'low_price': '0.02705000', 'taker_by_base_asset_volume': '98503.20000000', 'taker_by_quote_asset_volume': '2766.91140800'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715796, 'symbol': 'TOMOBTC', 'close_price': '0.00005045', 'open_price': '0.00004779', 'high_price': '0.00005048', 'low_price': '0.00004652', 'taker_by_base_asset_volume': '2978511.00000000', 'taker_by_quote_asset_volume': '144.42861171'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715535, 'symbol': 'TOMOUSDT', 'close_price': '0.46920000', 'open_price': '0.44930000', 'high_price': '0.47170000', 'low_price': '0.43000000', 'taker_by_base_asset_volume': '2175928.92000000', 'taker_by_quote_asset_volume': '983414.94253100'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715403, 'symbol': 'BEAMUSDT', 'close_price': '0.50340000', 'open_price': '0.49170000', 'high_price': '0.53000000', 'low_price': '0.48070000', 'taker_by_base_asset_volume': '2266897.49000000', 'taker_by_quote_asset_volume': '1148328.48354700'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715042, 'symbol': 'VITEBTC', 'close_price': '0.00000190', 'open_price': '0.00000184', 'high_price': '0.00000195', 'low_price': '0.00000173', 'taker_by_base_asset_volume': '35965553.00000000', 'taker_by_quote_asset_volume': '66.24169781'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715034, 'symbol': 'VITEUSDT', 'close_price': '0.01773000', 'open_price': '0.01730000', 'high_price': '0.01821000', 'low_price': '0.01606000', 'taker_by_base_asset_volume': '15621038.00000000', 'taker_by_quote_asset_volume': '268307.71989000'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715251, 'symbol': 'MBLBNB', 'close_price': '0.00011700', 'open_price': '0.00011350', 'high_price': '0.00011880', 'low_price': '0.00010980', 'taker_by_base_asset_volume': '83375259.00000000', 'taker_by_quote_asset_volume': '9505.73917390'}, {'stream_type': '!miniTicker@arr', 'event_type': '24hrMiniTicker', 'event_time': 1592594715431, 'symbol': 'KNCUSDT', 'close_price': '1.19900000', 'open_price': '1.15600000', 'high_price': '1.22400000', 'low_price': '1.14000000', 'taker_by_base_asset_volume': '939178.01300000', 'taker_by_quote_asset_volume': '1109490.22233400'}], 'unicorn_fied': ['binance.com', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_websocket(data)), asserted_result)

    def test_miniTicker_single(self):
        data = '{"stream":"btcusdt@miniTicker","data":{"e":"24hrMiniTicker","E":1601628771865,"s":"BTCUSDT","c":"10456.56000000","o":"10884.90000000","h":"10912.83000000","l":"10385.02000000","v":"64483.09756200","q":"685180788.34970800"}}'
        asserted_result = "{'stream_type': 'btcusdt@miniTicker', 'event_type': '24hrMiniTicker', 'data': [{'stream_type': 'btcusdt@miniTicker', 'event_type': '24hrMiniTicker', 'event_time': 1601628771865, 'symbol': 'BTCUSDT', 'close_price': '10456.56000000', 'open_price': '10884.90000000', 'high_price': '10912.83000000', 'low_price': '10385.02000000', 'taker_by_base_asset_volume': '64483.09756200', 'taker_by_quote_asset_volume': '685180788.34970800'}], 'unicorn_fied': ['binance.com', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_websocket(data)), asserted_result)

    def test_kline_1m(self):
        data = '{"stream":"btcusdt@kline_1m","data":{"e":"kline","E":1601630228469,"s":"BTCUSDT","k":{"t":1601630220000,"T":1601630279999,"s":"BTCUSDT","i":"1m","f":427033476,"L":427033658,"o":"10437.32000000","c":"10441.80000000","h":"10441.80000000","l":"10437.32000000","v":"20.63957400","n":183,"x":false,"q":"215452.69236872","V":"19.31210700","Q":"201593.99488069","B":"0"}}}'
        asserted_result = "{'stream_type': 'btcusdt@kline_1m', 'event_type': 'kline', 'event_time': 1601630228469, 'symbol': 'BTCUSDT', 'kline': {'kline_start_time': 1601630220000, 'kline_close_time': 1601630279999, 'symbol': 'BTCUSDT', 'interval': '1m', 'first_trade_id': False, 'last_trade_id': False, 'open_price': '10437.32000000', 'close_price': '10441.80000000', 'high_price': '10441.80000000', 'low_price': '10437.32000000', 'base_volume': '20.63957400', 'number_of_trades': 183, 'is_closed': False, 'quote': '215452.69236872', 'taker_by_base_asset_volume': '19.31210700', 'taker_by_quote_asset_volume': '201593.99488069', 'ignore': '0'}, 'unicorn_fied': ['binance.com', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_websocket(data)), asserted_result)

    def test_listStatus(self):
        data = '{"e":"listStatus","E":1606946194410,"s":"ETHUSDT","g":10717037,"c":"OCO","l":"ALL_DONE","L":"ALL_DONE","r":"NONE","C":"i8B7NXuB37QkJ2Vy8f5KHh","T":1606946194409,"O":[{"s":"ETHUSDT","i":2175939815,"c":"electron_648187c31bda49b6a2e81d23ae0"},{"s":"ETHUSDT","i":2175939816,"c":"84wruoWCZdkBUqbqlKfpv6"}]}'
        asserted_result = "{'stream_type': 'ethusdt@listStatus', 'event_type': 'listStatus', 'event_time': 1606946194410, 'symbol': 'ETHUSDT', 'order_list_id': 10717037, 'contingency_type': 'OCO', 'list_status_type': 'ALL_DONE', 'list_order_status': 'ALL_DONE', 'list_reject_reason': 'NONE', 'list_client_order_id': 'i8B7NXuB37QkJ2Vy8f5KHh', 'transaction_time': 1606946194409, 'objects': [{'symbol': 'ETHUSDT', 'order_id': 2175939815, 'client_order_id': 'electron_648187c31bda49b6a2e81d23ae0'}, {'symbol': 'ETHUSDT', 'order_id': 2175939816, 'client_order_id': '84wruoWCZdkBUqbqlKfpv6'}], 'unicorn_fied': ['binance.com', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_websocket(data)), asserted_result)

    def test_balanceUpdate(self):
        data = '{"e":"balanceUpdate","E":1615926131286,"a":"USDT","d":"1.00000000","T":1615926131285}'
        asserted_result = "{'stream_type': '!userData@arr', 'event_type': 'balanceUpdate', 'event_time': 1615926131286, 'asset': 'USDT', 'balance_delta': '1.00000000', 'clear_time': 1615926131285, 'unicorn_fied': ['binance.com', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_websocket(data)), asserted_result)

    def test_template(self):
        data = ''
        asserted_result = "" + self.unicorn_fy_version + "']}"
        #self.assertEqual(str(self.unicorn_fy.binance_com_websocket(data)), asserted_result)

    def tearDown(self):
        del self.unicorn_fy


class TestBinanceComWebsocketFutures(unittest.TestCase):
    def setUp(self):
        self.unicorn_fy = UnicornFy()
        self.unicorn_fy_version = str(self.unicorn_fy.get_version())
        self.unicorn_fy.binance_futures_websocket("data", show_deprecated_warning=True)
        
    def test_update(self):
        self.assertFalse(self.unicorn_fy.is_update_available())

    def test_with_non_json(self):
        self.unicorn_fy.binance_futures_websocket(False)

    def test_result(self):
        data = '{"result":null,"id":2}'
        asserted_result = "{'result': None, 'id': 2, 'unicorn_fied': ['binance.com', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_websocket(data)), asserted_result)

    def test_error(self):
        data = '{"error":"blahblah"}'
        asserted_result = "{'error': 'blahblah', 'unicorn_fied': ['binance.com', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_websocket(data)), asserted_result)

    def test_aggTrade_single(self):
        data = '{"stream":"btcusdt@aggTrade","data":{"e":"aggTrade","E":1592584651517,"s":"BTCUSDT","a":315753210,"p":"9319.00000000","q":"0.01864900","f":343675554,"l":343675554,"T":1592584651516,"m":true,"M":true}}'
        asserted_result = "{'stream_type': 'btcusdt@aggTrade', 'event_type': 'aggTrade', 'event_time': 1592584651517, 'symbol': 'BTCUSDT', 'aggregate_trade_id': 315753210, 'price': '9319.00000000', 'quantity': '0.01864900', 'first_trade_id': 343675554, 'last_trade_id': 343675554, 'trade_time': 1592584651516, 'is_market_maker': True, 'unicorn_fied': ['binance.com-futures', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_futures_websocket(data)), asserted_result)

    def test_account_update_futures(self):
        data = '{"e":"ACCOUNT_UPDATE","T":1617859763506,"E":1617859763511,"a":{"B":[{"a":"USDT","wb":"1790.86605837","cw":"1790.86605837"}],"P":[{"s":"CHZUSDT","pa":"0","ep":"0.00000","cr":"0","up":"0","mt":"cross","iw":"0","ps":"BOTH","ma":"USDT"},{"s":"CHZUSDT","pa":"2684","ep":"0.45855","cr":"79.89127995","up":"2.03986684","mt":"cross","iw":"0","ps":"LONG","ma":"USDT"}],"m":"ORDER"}}'
        asserted_result = "{'stream_type': 'ACCOUNT_UPDATE', 'event_type': 'ACCOUNT_UPDATE', 'event_time': 1617859763511, 'transaction': 1617859763506, 'event_reason': 'ORDER', 'balances': [{'asset': 'USDT', 'wallet_balance': '1790.86605837', 'cross_wallet_balance': '1790.86605837'}], 'positions': [{'symbol': 'CHZUSDT', 'position_amount': '0', 'entry_price': '0.00000', 'accumulated_realized': '0', 'upnl': '0', 'margin_type': 'cross', 'isolated_wallet': '0', 'position_side': 'BOTH'}, {'symbol': 'CHZUSDT', 'position_amount': '2684', 'entry_price': '0.45855', 'accumulated_realized': '79.89127995', 'upnl': '2.03986684', 'margin_type': 'cross', 'isolated_wallet': '0', 'position_side': 'LONG'}], 'unicorn_fied': ['binance.com-futures', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_futures_websocket(data)), asserted_result)

    def test_order_trade_update_futures(self):
        data = '{"e":"ORDER_TRADE_UPDATE","T":1617859867769,"E":1617859867772,"o":{"s":"SANDUSDT","c":"electron_6LyJZ9KPgmRbhKfFamx3","S":"BUY","o":"LIMIT","f":"GTC","q":"1000","p":"0.63428","ap":"0","sp":"0","x":"NEW","X":"NEW","i":315803079,"l":"0","z":"0","L":"0","T":1617859867769,"t":0,"b":"1262.16000","a":"0","m":false,"R":false,"wt":"CONTRACT_PRICE","ot":"LIMIT","ps":"LONG","cp":false,"rp":"0","pP":false,"si":0,"ss":0}}'
        asserted_result = "{'stream_type': 'ORDER_TRADE_UPDATE', 'event_type': 'ORDER_TRADE_UPDATE', 'event_time': 1617859867772, 'symbol': 'SANDUSDT', 'client_order_id': 'electron_6LyJZ9KPgmRbhKfFamx3', 'side': 'BUY', 'order_type': 'LIMIT', 'time_in_force': 'GTC', 'order_quantity': '1000', 'order_price': '0.63428', 'order_avg_price': '0', 'order_stop_price': '0', 'current_execution_type': 'NEW', 'current_order_status': 'NEW', 'order_id': 315803079, 'last_executed_quantity': '0', 'cumulative_filled_quantity': '0', 'last_executed_price': '0', 'transaction_time': 1617859867769, 'trade_id': 0, 'net_pay': '1262.16000', 'net_selling_order_value': '0', 'is_trade_maker_side': False, 'reduce_only': False, 'trigger_price_type': 'CONTRACT_PRICE', 'order_price_type': 'LIMIT', 'position_side': 'LONG', 'order_realized_profit': '0', 'unicorn_fied': ['binance.com-futures', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_futures_websocket(data)), asserted_result)

    def test_depth_futures(self):
        data = '{"stream":"btcusdt@depth","data":{"e":"depthUpdate","E":1644317757646,"s":"BTCUSDT","U":16895904809,"u":16895904977,"b":[["43903.04000000","0.00000000"],["43902.20000000","0.00000000"],["43900.53000000","0.42450000"],["43900.52000000","0.01139000"],["43899.30000000","0.01412000"],["43899.04000000","0.00000000"],["43899.03000000","0.00000000"],["43898.28000000","0.07745000"],["43898.27000000","0.00000000"],["43898.26000000","0.00000000"],["43898.19000000","0.00000000"],["43898.11000000","0.12661000"],["43898.10000000","0.00000000"],["43897.39000000","0.11799000"],["43897.38000000","0.11380000"],["43897.35000000","0.00000000"],["43897.34000000","0.00000000"],["43897.33000000","0.00000000"],["43897.32000000","0.00000000"],["43897.09000000","0.00000000"],["43896.13000000","0.13600000"],["43895.39000000","0.21690000"],["43895.28000000","0.00000000"],["43895.19000000","0.00000000"],["43894.59000000","0.14798000"],["43894.43000000","0.00000000"],["43892.97000000","0.00000000"],["43892.86000000","0.02500000"],["43891.82000000","0.00000000"],["43891.81000000","0.03416000"],["43891.74000000","0.19998000"],["43891.65000000","0.00000000"],["43891.47000000","0.00000000"],["43891.46000000","0.00000000"],["43891.45000000","0.00000000"],["43891.00000000","0.00000000"],["43890.27000000","0.00000000"],["43889.64000000","0.15000000"],["43889.37000000","0.00000000"],["43888.77000000","0.22142000"],["43888.76000000","0.00000000"],["43887.91000000","0.74700000"],["43887.82000000","0.00000000"],["43886.71000000","0.00000000"],["43886.55000000","0.00000000"],["43885.28000000","0.05456000"],["43885.25000000","0.00000000"],["43884.03000000","0.00000000"],["43883.84000000","0.00120000"],["43882.33000000","0.00000000"],["43880.68000000","0.00000000"],["43878.28000000","0.08000000"],["43875.11000000","0.12000000"],["43874.26000000","0.20000000"],["43873.17000000","0.40000000"],["43863.76000000","0.00000000"],["43862.20000000","0.00000000"],["43857.88000000","0.18233000"],["43842.25000000","0.00000000"],["43730.76000000","0.00000000"]],"a":[["43900.54000000","0.01080000"],["43900.85000000","0.00000000"],["43903.04000000","0.00000000"],["43903.05000000","0.00000000"],["43903.50000000","0.04639000"],["43904.41000000","0.06674000"],["43904.94000000","0.13600000"],["43905.79000000","0.00000000"],["43906.86000000","0.00000000"],["43907.99000000","0.00000000"],["43908.06000000","0.00000000"],["43908.29000000","0.01708000"],["43909.01000000","0.00000000"],["43909.22000000","0.01708000"],["43909.29000000","0.11923000"],["43909.30000000","0.14798000"],["43909.31000000","0.14999000"],["43909.47000000","0.01707000"],["43910.23000000","0.00000000"],["43910.43000000","0.00000000"],["43910.50000000","0.00000000"],["43910.51000000","0.46800000"],["43910.52000000","0.00000000"],["43910.58000000","0.00000000"],["43910.59000000","0.00000000"],["43910.67000000","0.00000000"],["43911.46000000","0.00000000"],["43912.00000000","0.18783000"],["43912.01000000","0.00000000"],["43912.68000000","0.31941000"],["43914.14000000","0.00000000"],["43914.44000000","0.11380000"],["43916.35000000","0.26713000"],["43921.30000000","0.00000000"],["43923.12000000","0.00000000"],["43923.36000000","0.00120000"],["43935.57000000","0.23677000"],["43935.81000000","0.02274000"],["43942.76000000","0.00000000"],["43950.46000000","0.00000000"],["44016.76000000","0.00000000"],["44500.00000000","7.91139000"]]}}'
        asserted_result = "{'stream_type': 'btcusdt@depth', 'event_type': 'depthUpdate', 'event_time': 1644317757646, 'symbol': 'BTCUSDT', 'first_update_id_in_event': 16895904809, 'final_update_id_in_event': 16895904977, 'asks': [['43900.54000000', '0.01080000'], ['43900.85000000', '0.00000000'], ['43903.04000000', '0.00000000'], ['43903.05000000', '0.00000000'], ['43903.50000000', '0.04639000'], ['43904.41000000', '0.06674000'], ['43904.94000000', '0.13600000'], ['43905.79000000', '0.00000000'], ['43906.86000000', '0.00000000'], ['43907.99000000', '0.00000000'], ['43908.06000000', '0.00000000'], ['43908.29000000', '0.01708000'], ['43909.01000000', '0.00000000'], ['43909.22000000', '0.01708000'], ['43909.29000000', '0.11923000'], ['43909.30000000', '0.14798000'], ['43909.31000000', '0.14999000'], ['43909.47000000', '0.01707000'], ['43910.23000000', '0.00000000'], ['43910.43000000', '0.00000000'], ['43910.50000000', '0.00000000'], ['43910.51000000', '0.46800000'], ['43910.52000000', '0.00000000'], ['43910.58000000', '0.00000000'], ['43910.59000000', '0.00000000'], ['43910.67000000', '0.00000000'], ['43911.46000000', '0.00000000'], ['43912.00000000', '0.18783000'], ['43912.01000000', '0.00000000'], ['43912.68000000', '0.31941000'], ['43914.14000000', '0.00000000'], ['43914.44000000', '0.11380000'], ['43916.35000000', '0.26713000'], ['43921.30000000', '0.00000000'], ['43923.12000000', '0.00000000'], ['43923.36000000', '0.00120000'], ['43935.57000000', '0.23677000'], ['43935.81000000', '0.02274000'], ['43942.76000000', '0.00000000'], ['43950.46000000', '0.00000000'], ['44016.76000000', '0.00000000'], ['44500.00000000', '7.91139000']], 'unicorn_fied': ['binance.com-futures', '0.12.0.dev']}"

        self.assertEqual(str(self.unicorn_fy.binance_com_futures_websocket(data)), asserted_result)

    def test_margin_call_futures(self):
        # Todo: MISSING!!!
        pass

    def test_account_config_update_futures(self):
        data = '{"e":"ACCOUNT_CONFIG_UPDATE","T":1617971759717,"E":1617971759721,"ac":{"s":"BTCUSDT","l":19}}'
        asserted_result = "{'stream_type': 'ACCOUNT_CONFIG_UPDATE', 'event_type': 'ACCOUNT_CONFIG_UPDATE', 'event_time': 1617971759721, 'symbol': 'BTCUSDT', 'leverage': 19, 'unicorn_fied': ['binance.com-futures', '" + self.unicorn_fy_version + "']}"
        self.assertEqual(str(self.unicorn_fy.binance_com_futures_websocket(data)), asserted_result)

    def tearDown(self):
        del self.unicorn_fy


class TestBinanceComMarginWebsocket(unittest.TestCase):
    def setUp(self):
        self.unicorn_fy = UnicornFy()
        self.unicorn_fy_version = str(self.unicorn_fy.get_version())

    def test_template(self):
        data = ''
        asserted_result = ""
        self.assertEqual(str(self.unicorn_fy.binance_com_margin_websocket(data)), asserted_result)

    def tearDown(self):
        del self.unicorn_fy


class TestBinanceComIsolatedMarginWebsocket(unittest.TestCase):
    def setUp(self):
        self.unicorn_fy = UnicornFy()
        self.unicorn_fy_version = str(self.unicorn_fy.get_version())

    def test_template(self):
        data = ''
        asserted_result = ""
        self.assertEqual(str(self.unicorn_fy.binance_com_isolated_margin_websocket(data)), asserted_result)

    def tearDown(self):
        del self.unicorn_fy


class TestBinanceJeWebsocket(unittest.TestCase):
    def setUp(self):
        self.unicorn_fy = UnicornFy()
        self.unicorn_fy_version = str(self.unicorn_fy.get_version())

    def test_template(self):
        data = ''
        asserted_result = ""
        self.assertEqual(str(self.unicorn_fy.binance_je_websocket(data)), asserted_result)

    def tearDown(self):
        del self.unicorn_fy


class TestBinanceJexWebsocket(unittest.TestCase):
    def setUp(self):
        self.unicorn_fy = UnicornFy()
        self.unicorn_fy_version = str(self.unicorn_fy.get_version())

    def test_template(self):
        data = ''
        asserted_result = ""
        self.assertEqual(str(self.unicorn_fy.jex_com_websocket(data)), asserted_result)

    def tearDown(self):
        del self.unicorn_fy


class TestBinanceUsWebsocket(unittest.TestCase):
    def setUp(self):
        self.unicorn_fy = UnicornFy()
        self.unicorn_fy_version = str(self.unicorn_fy.get_version())

    def test_template(self):
        data = ''
        asserted_result = ""
        self.assertEqual(str(self.unicorn_fy.binance_us_websocket(data)), asserted_result)

    def tearDown(self):
        del self.unicorn_fy


class TestBinanceTRWebsocket(unittest.TestCase):
    def setUp(self):
        self.unicorn_fy = UnicornFy()
        self.unicorn_fy_version = str(self.unicorn_fy.get_version())

    def test_template(self):
        data = ''
        asserted_result = ""
        self.assertEqual(str(self.unicorn_fy.trbinance_com_websocket(data)), asserted_result)

    def tearDown(self):
        del self.unicorn_fy


class TestBinanceOrgWebsocket(unittest.TestCase):
    def setUp(self):
        self.unicorn_fy = UnicornFy()
        self.unicorn_fy_version = str(self.unicorn_fy.get_version())

    def test_template(self):
        data = ''
        asserted_result = ""
        self.assertEqual(str(self.unicorn_fy.binance_org_websocket(data)), asserted_result)

    def tearDown(self):
        del self.unicorn_fy


class TestLiveBinanceCom(unittest.TestCase):
    def setUp(self):
        print("\n\rStarting live test binance.com")
        self.unicorn_fy = UnicornFy()
        ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
        worker_thread = threading.Thread(target=print_stream_data_from_stream_buffer,
                                         args=(ubwa,))
        worker_thread.start()

        channels = {'aggTrade', 'trade', 'kline_1m', 'kline_5m', 'kline_15m', 'kline_30m', 'kline_1h', 'kline_2h',
                    'kline_4h',
                    'kline_6h', 'kline_8h', 'kline_12h', 'kline_1d', 'kline_3d', 'kline_1w', 'kline_1M', 'miniTicker',
                    'ticker', 'bookTicker', 'depth5', 'depth10', 'depth20', 'depth', 'depth@100ms'}
        arr_channels = {'!miniTicker', '!ticker', '!bookTicker'}
        markets = {'bnbbtc', 'ethbtc', 'btcusdt', 'bchabcusdt', 'xrpusdt', 'rvnbtc', 'ltcusdt', 'adausdt', 'eosusdt',
                   'wanbnb', 'zrxbnb', 'agibnb', 'funeth', 'arketh', 'engeth'}
        for channel in channels:
            ubwa.create_stream(channel, markets, stream_label=channel)
        ubwa.create_stream(arr_channels, "arr")
        stream_id_trade = ubwa.get_stream_id_by_label("trade")
        ubwa.get_stream_subscriptions(stream_id_trade)
        time.sleep(70)
        ubwa.stop_manager_with_all_streams()

    def test_template(self):
        data = ''
        asserted_result = ""
        self.assertEqual(str(self.unicorn_fy.binance_org_websocket(data)), asserted_result)

    def tearDown(self):
        del self.unicorn_fy


class TestLiveBinanceComFutures(unittest.TestCase):
    def setUp(self):
        print("\n\rStarting live test binance.com-futures")
        self.unicorn_fy = UnicornFy()
        ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com-futures")
        worker_thread = threading.Thread(target=print_stream_data_from_stream_buffer_futures,
                                         args=(ubwa,))
        worker_thread.start()

        channels = {'aggTrade', 'trade', 'kline_1m', 'kline_5m', 'kline_15m', 'kline_30m', 'kline_1h', 'kline_2h',
                    'kline_4h',
                    'kline_6h', 'kline_8h', 'kline_12h', 'kline_1d', 'kline_3d', 'kline_1w', 'kline_1M', 'miniTicker',
                    'ticker', 'bookTicker', 'depth5', 'depth10', 'depth20', 'depth', 'depth@100ms'}
        arr_channels = {'!miniTicker', '!ticker', '!bookTicker'}
        markets = {'bnbbtc', 'ethbtc', 'btcusdt', 'bchabcusdt', 'xrpusdt', 'rvnbtc', 'ltcusdt', 'adausdt', 'eosusdt',
                   'wanbnb', 'zrxbnb', 'agibnb', 'funeth', 'arketh', 'engeth'}
        for channel in channels:
            ubwa.create_stream(channel, markets, stream_label=channel)
        ubwa.create_stream(arr_channels, "arr")
        stream_id_trade = ubwa.get_stream_id_by_label("trade")
        ubwa.get_stream_subscriptions(stream_id_trade)
        time.sleep(70)
        ubwa.stop_manager_with_all_streams()

    def test_template(self):
        data = ''
        asserted_result = ""
        self.assertEqual(str(self.unicorn_fy.binance_org_websocket(data)), asserted_result)

    def tearDown(self):
        del self.unicorn_fy


if __name__ == '__main__':
    unittest.main()

