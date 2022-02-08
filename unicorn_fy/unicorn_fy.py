#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File: unicorn_fy/unicorn_fy.py
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

import logging
import time

import requests
import ujson as json

logger = logging.getLogger("unicorn_fy")


class UnicornFy(object):
    """
    Unify received data from crypto exchanges

    Supported exchanges:
        - Binance.com
        - Binance-com-futures
        - Binance-com-coin_futures
        - Binance-com-margin
        - Binance-com-isolated_margin
        - Binance.je
        - Binance.us
        - trBinance.com
        - Binance.org
        - Jex.com
    """
    VERSION = "0.11.1"

    def __init__(self):
        self.last_update_check_github = {'timestamp': time.time(),
                                         'status': None}

    @staticmethod
    def binance_org_websocket(stream_data_json):
        """
        unicorn_fy binance.org (incl testnet) raw_stream_data

        :param stream_data_json: The received raw stream data from the Binance websocket
        :type stream_data_json: json

        :return: dict
        """
        logger.info("Can not convert raw data from binance.org")
        return stream_data_json

    @staticmethod
    def binance_com_websocket(stream_data_json):
        """
        unicorn_fy binance.com raw_stream_data

        :param stream_data_json: The received raw stream data from the Binance websocket
        :type stream_data_json: json

        :return: dict
        """
        return UnicornFy.binance_websocket(stream_data_json, exchange="binance.com", show_deprecated_warning=False)

    @staticmethod
    def binance_com_margin_websocket(stream_data_json):
        """
        unicorn_fy binance.com-margin raw_stream_data

        :param stream_data_json: The received raw stream data from the Binance websocket
        :type stream_data_json: json

        :return: dict
        """
        return UnicornFy.binance_websocket(stream_data_json, exchange="binance.com-margin",
                                           show_deprecated_warning=False)

    @staticmethod
    def binance_com_isolated_margin_websocket(stream_data_json):
        """
        unicorn_fy binance.com-isolated_margin raw_stream_data

        :param stream_data_json: The received raw stream data from the Binance websocket
        :type stream_data_json: json

        :return: dict
        """
        return UnicornFy.binance_websocket(stream_data_json,
                                           exchange="binance.com-isolated_margin",
                                           show_deprecated_warning=False)

    @staticmethod
    def binance_com_futures_websocket(stream_data_json):
        """
        unicorn_fy binance.com-futures raw_stream_data

        :param stream_data_json: The received raw stream data from the Binance websocket
        :type stream_data_json: json

        :return: dict
        """
        return UnicornFy.binance_futures_websocket(stream_data_json,
                                                   exchange="binance.com-futures",
                                                   show_deprecated_warning=False)

    @staticmethod
    def binance_com_coin_futures_websocket(stream_data_json):
        """
        unicorn_fy binance.com-coin_futures raw_stream_data

        :param stream_data_json: The received raw stream data from the Binance websocket
        :type stream_data_json: json

        :return: dict
        """
        return UnicornFy.binance_coin_futures_websocket(stream_data_json,
                                                        exchange="binance.com-coin_futures",
                                                        show_deprecated_warning=False)

    @staticmethod
    def binance_je_websocket(stream_data_json):
        """
        unicorn_fy binance.je (Jersey) raw_stream_data

        :param stream_data_json: The received raw stream data from the Binance websocket
        :type stream_data_json: json

        :return: dict
        """
        return UnicornFy.binance_websocket(stream_data_json, exchange="binance.je", show_deprecated_warning=False)

    @staticmethod
    def binance_us_websocket(stream_data_json):
        """
        unicorn_fy binance.us (US) raw_stream_data

        :param stream_data_json: The received raw stream data from the Binance websocket
        :type stream_data_json: json

        :return: dict
        """
        return UnicornFy.binance_websocket(stream_data_json, exchange="binance.us", show_deprecated_warning=False)

    @staticmethod
    def trbinance_com_websocket(stream_data_json):
        """
        unicorn_fy trbinance.com (TR) raw_stream_data

        :param stream_data_json: The received raw stream data from the Binance websocket
        :type stream_data_json: json

        :return: dict
        """
        return UnicornFy.binance_websocket(stream_data_json, exchange="trbinance.com", show_deprecated_warning=False)

    @staticmethod
    def binance_websocket(stream_data_json, exchange="binance", show_deprecated_warning=True):
        """
        unicorn_fy binance.com raw_stream_data

        :param stream_data_json: The received raw stream data from the Binance websocket
        :type stream_data_json: json

        :param exchange: Exchange endpoint.
        :type exchange: str

        :param show_deprecated_warning: Show or hide warning
        :type show_deprecated_warning: bool

        :return: dict
        """
        unicorn_fied_data = False

        logger.debug("UnicornFy->binance_websocket(" + str(stream_data_json) + ")")
        if show_deprecated_warning is True:
            logger.warning("Using `UnicornFy.binance_websocket()` is deprecated, use "
                           "`UnicornFy.binance_com_websocket()`, `binance_futures_websocket()` or "
                           "`UnicornFy.binance_je_websocket()` instead!")

        if UnicornFy.is_json(stream_data_json) is False:
            return stream_data_json

        stream_data = json.loads(stream_data_json)

        try:
            if stream_data[0]['e'] == "24hrMiniTicker":
                stream_data = {'data': {'e': "24hrMiniTicker"},
                               'items': stream_data}
            elif stream_data[0]['e'] == "24hrTicker":
                stream_data = {'data': {'e': "24hrTicker"},
                               'items': stream_data}
        except KeyError:
            pass

        try:
            if "!ticker@arr" in stream_data['stream']:
                stream_data = {'data': {'e': "24hrTicker"},
                               'items': stream_data['data']}
            elif "!miniTicker@arr" in stream_data['stream']:
                stream_data = {'data': {'e': "24hrMiniTicker"},
                               'items': stream_data['data']}
        except KeyError:
            pass

        try:
            if stream_data['e'] == 'outboundAccountInfo':
                stream_data = {'data': stream_data}
            elif stream_data['e'] == 'executionReport':
                stream_data = {'data': stream_data}
            elif stream_data['e'] == 'outboundAccountPosition':
                stream_data = {'data': stream_data}
            elif stream_data['e'] == 'listStatus':
                stream_data = {'data': stream_data}
            elif stream_data['e'] == 'balanceUpdate':
                stream_data = {'data': stream_data}
        except KeyError:
            pass
        try:
            if stream_data['stream'].find('@depth5') != -1:
                stream_data['data']['e'] = "depth"
                stream_data['data']['depth_level'] = 5
            elif stream_data['stream'].find('@depth10') != -1:
                stream_data['data']['e'] = "depth"
                stream_data['data']['depth_level'] = 10
            elif stream_data['stream'].find('@depth20') != -1:
                stream_data['data']['e'] = "depth"
                stream_data['data']['depth_level'] = 20
            elif "@bookTicker" in stream_data['stream']:
                stream_data['data']['e'] = "bookTicker"
        except KeyError:
            pass

        try:
            # return if already unicorn_fied
            if stream_data['unicorn_fied']:
                return stream_data
        except KeyError:
            pass

        try:
            if stream_data['result'] is None:
                unicorn_fied_version = [exchange, UnicornFy.VERSION]
                stream_data['unicorn_fied'] = unicorn_fied_version
                logger.debug(f"UnicornFy->binance_websocket({str(stream_data)}, {str(exchange)}")
                return stream_data
            else:
                unicorn_fied_version = [exchange, UnicornFy.VERSION]
                stream_data['unicorn_fied'] = unicorn_fied_version
                logger.debug(f"UnicornFy->binance_websocket({str(stream_data)}, {str(exchange)}")
                return stream_data
        except KeyError:
            pass

        try:
            if stream_data['error']:
                unicorn_fied_version = [exchange, UnicornFy.VERSION]
                stream_data['unicorn_fied'] = unicorn_fied_version
                logger.debug(f"UnicornFy->binance_websocket({str(stream_data)}, {str(exchange)}")
                return stream_data
        except KeyError:
            pass

        if stream_data['data']['e'] == 'aggTrade':
            unicorn_fied_data = {'stream_type': stream_data['stream'],
                                 'event_type': stream_data['data']['e'],
                                 'event_time': stream_data['data']['E'],
                                 'symbol': stream_data['data']['s'],
                                 'aggregate_trade_id': stream_data['data']['a'],
                                 'price': stream_data['data']['p'],
                                 'quantity': stream_data['data']['q'],
                                 'first_trade_id': stream_data['data']['f'],
                                 'last_trade_id': stream_data['data']['l'],
                                 'trade_time': stream_data['data']['T'],
                                 'is_market_maker': stream_data['data']['m'],
                                 'ignore': stream_data['data']['M']}
        elif stream_data['data']['e'] == 'listStatus':
            objects = []
            for item in stream_data['data']['O']:
                objects.append({'symbol': item['s'],
                                'order_id': item['i'],
                                'client_order_id': item['c']})
            unicorn_fied_data = {'stream_type': stream_data['data']['s'].lower() + "@listStatus",
                                 'event_type': stream_data['data']['e'],
                                 'event_time': stream_data['data']['E'],
                                 'symbol': stream_data['data']['s'],
                                 'order_list_id': stream_data['data']['g'],
                                 'contingency_type': stream_data['data']['c'],
                                 'list_status_type': stream_data['data']['l'],
                                 'list_order_status': stream_data['data']['L'],
                                 'list_reject_reason': stream_data['data']['r'],
                                 'list_client_order_id': stream_data['data']['C'],
                                 'transaction_time': stream_data['data']['T'],
                                 'objects': objects}
        elif stream_data['data']['e'] == 'trade':
            unicorn_fied_data = {'stream_type': stream_data['stream'],
                                 'event_type': stream_data['data']['e'],
                                 'event_time': stream_data['data']['E'],
                                 'symbol': stream_data['data']['s'],
                                 'trade_id': stream_data['data']['t'],
                                 'price': stream_data['data']['p'],
                                 'quantity': stream_data['data']['q'],
                                 'buyer_order_id': stream_data['data']['b'],
                                 'seller_order_id': stream_data['data']['a'],
                                 'trade_time': stream_data['data']['T'],
                                 'is_market_maker': stream_data['data']['m'],
                                 'ignore': stream_data['data']['M']}
        elif stream_data['data']['e'] == 'bookTicker':
            unicorn_fied_data = {'stream_type': stream_data['stream'],
                                 'order_book_update_id': stream_data['data']['u'],
                                 'symbol': stream_data['data']['s'],
                                 'best_bid_price': stream_data['data']['b'],
                                 'best_bid_quantity': stream_data['data']['B'],
                                 'best_ask_price': stream_data['data']['a'],
                                 'best_ask_quantity': stream_data['data']['A'],
                                 'event_type': stream_data['data']['e']}
        elif stream_data['data']['e'] == 'kline':
            stream_data['data'] = UnicornFy.set_to_false_if_not_exist(stream_data['data'], 'f')
            stream_data['data'] = UnicornFy.set_to_false_if_not_exist(stream_data['data'], 'L')
            unicorn_fied_data = {'stream_type': stream_data['stream'],
                                 'event_type': stream_data['data']['e'],
                                 'event_time': stream_data['data']['E'],
                                 'symbol': stream_data['data']['s'],
                                 'kline': {'kline_start_time': stream_data['data']['k']['t'],
                                           'kline_close_time': stream_data['data']['k']['T'],
                                           'symbol': stream_data['data']['k']['s'],
                                           'interval': stream_data['data']['k']['i'],
                                           'first_trade_id': stream_data['data']['f'],
                                           'last_trade_id': stream_data['data']['L'],
                                           'open_price': stream_data['data']['k']['o'],
                                           'close_price': stream_data['data']['k']['c'],
                                           'high_price': stream_data['data']['k']['h'],
                                           'low_price': stream_data['data']['k']['l'],
                                           'base_volume': stream_data['data']['k']['v'],
                                           'number_of_trades': stream_data['data']['k']['n'],
                                           'is_closed': stream_data['data']['k']['x'],
                                           'quote': stream_data['data']['k']['q'],
                                           'taker_by_base_asset_volume': stream_data['data']['k']['V'],
                                           'taker_by_quote_asset_volume': stream_data['data']['k']['Q'],
                                           'ignore': stream_data['data']['k']['B']}}
        elif stream_data['data']['e'] == '24hrMiniTicker':
            try:
                if stream_data['stream']:
                    pass
            except KeyError:
                stream_data['stream'] = '!miniTicker@arr'
            unicorn_fied_data = {'stream_type': stream_data['stream'],
                                 'event_type': stream_data['data']['e'],
                                 'data': []}

            try:
                for item in stream_data['items']:
                    data = {'stream_type': stream_data['stream'],
                            'event_type': item['e'],
                            'event_time': item['E'],
                            'symbol': item['s'],
                            'close_price': item['c'],
                            'open_price': item['o'],
                            'high_price': item['h'],
                            'low_price': item['l'],
                            'taker_by_base_asset_volume': item['v'],
                            'taker_by_quote_asset_volume': item['q']}
                    unicorn_fied_data['data'].append(data)
            except KeyError:
                try:
                    data = {'stream_type': stream_data['stream'],
                            'event_type': stream_data['data']['e'],
                            'event_time': stream_data['data']['E'],
                            'symbol': stream_data['data']['s'],
                            'close_price': stream_data['data']['c'],
                            'open_price': stream_data['data']['o'],
                            'high_price': stream_data['data']['h'],
                            'low_price': stream_data['data']['l'],
                            'taker_by_base_asset_volume': stream_data['data']['v'],
                            'taker_by_quote_asset_volume': stream_data['data']['q']}
                    unicorn_fied_data['data'].append(data)
                except KeyError as error_msg:
                    logger.critical(f"UnicornFy->binance_com_futures_websocket({str(stream_data)}) - "
                                    f"error: {str(error_msg)}")
                    print(str(stream_data))
        elif stream_data['data']['e'] == '24hrTicker':
            try:
                if stream_data['stream']:
                    pass
            except KeyError:
                stream_data['stream'] = '!ticker@arr'
            unicorn_fied_data = {'stream_type': stream_data['stream'],
                                 'event_type': stream_data['data']['e'],
                                 'data': []}
            try:
                for item in stream_data['items']:
                    data = {'stream_type': stream_data['stream'],
                            'event_type': item['e'],
                            'event_time': item['E'],
                            'symbol': item['s'],
                            'price_change': item['p'],
                            'price_change_percent': item['P'],
                            'weighted_average_price': item['w'],
                            'trade_before_24h_window': item['x'],
                            'last_price': item['c'],
                            'last_quantity': item['Q'],
                            'best_bid_price': item['b'],
                            'best_bid_quantity': item['B'],
                            'best_ask_price': item['a'],
                            'best_ask_quantity': item['A'],
                            'open_price': item['o'],
                            'high_price': item['h'],
                            'low_price': item['l'],
                            'total_traded_base_asset_volume': item['v'],
                            'total_traded_quote_asset_volume': item['q'],
                            'statistics_open_time': item['O'],
                            'statistics_close_time': item['C'],
                            'first_trade_id': item['F'],
                            'last_trade_id': item['L'],
                            'total_nr_of_trades': item['n']}
                    unicorn_fied_data['data'].append(data)
            except KeyError:
                data = {'stream_type': stream_data['stream'],
                        'event_type': stream_data['data']['e'],
                        'event_time': stream_data['data']['E'],
                        'symbol': stream_data['data']['s'],
                        'price_change': stream_data['data']['p'],
                        'price_change_percent': stream_data['data']['P'],
                        'weighted_average_price': stream_data['data']['w'],
                        'trade_before_24h_window': stream_data['data']['x'],
                        'last_price': stream_data['data']['c'],
                        'last_quantity': stream_data['data']['Q'],
                        'best_bid_price': stream_data['data']['b'],
                        'best_bid_quantity': stream_data['data']['B'],
                        'best_ask_price': stream_data['data']['a'],
                        'best_ask_quantity': stream_data['data']['A'],
                        'open_price': stream_data['data']['o'],
                        'high_price': stream_data['data']['h'],
                        'low_price': stream_data['data']['l'],
                        'total_traded_base_asset_volume': stream_data['data']['v'],
                        'total_traded_quote_asset_volume': stream_data['data']['q'],
                        'statistics_open_time': stream_data['data']['O'],
                        'statistics_close_time': stream_data['data']['C'],
                        'first_trade_id': stream_data['data']['F'],
                        'last_trade_id': stream_data['data']['L'],
                        'total_nr_of_trades': stream_data['data']['n']}
                unicorn_fied_data['data'].append(data)
        elif stream_data['data']['e'] == 'depth':
            unicorn_fied_data = {'stream_type': stream_data['stream'],
                                 'event_type': stream_data['data']['e'],
                                 'symbol': stream_data['stream'][:stream_data['stream'].find('@')].upper(),
                                 'last_update_id': stream_data['data']['lastUpdateId'],
                                 'bids': stream_data['data']['bids'],
                                 'asks': stream_data['data']['asks']}
        elif stream_data['data']['e'] == 'depthUpdate':
            unicorn_fied_data = {'stream_type': stream_data['stream'],
                                 'event_type': stream_data['data']['e'],
                                 'event_time': stream_data['data']['E'],
                                 'symbol': stream_data['data']['s'],
                                 'first_update_id_in_event': stream_data['data']['U'],
                                 'final_update_id_in_event': stream_data['data']['u'],
                                 'bids': stream_data['data']['b'],
                                 'asks': stream_data['data']['a']}
        elif stream_data['data']['e'] == 'outboundAccountInfo':
            unicorn_fied_data = {'stream_type': '!userData@arr',
                                 'event_type': stream_data['data']['e'],
                                 'event_time': stream_data['data']['E'],
                                 'maker_commission_rate': stream_data['data']['m'],
                                 'taker_commission_rate': stream_data['data']['t'],
                                 'buyer_commission_rate': stream_data['data']['b'],
                                 'seller_commission_rate': stream_data['data']['s'],
                                 'can_trade': stream_data['data']['T'],
                                 'can_withdraw': stream_data['data']['W'],
                                 'can_deposit': stream_data['data']['D'],
                                 'balances': [],
                                 'account_permissions': stream_data['data']['P']}
            for item in stream_data['data']['B']:
                new_item = {'asset': item['a'],
                            'free': item['f'],
                            'locked': item['l']}
                unicorn_fied_data['balances'] += [new_item]
        elif stream_data['data']['e'] == 'outboundAccountPosition':
            unicorn_fied_data = {'stream_type': '!userData@arr',
                                 'event_type': stream_data['data']['e'],
                                 'event_time': stream_data['data']['E'],
                                 'last_update_time': stream_data['data']['u'],
                                 'balances': []}
            for item in stream_data['data']['B']:
                new_item = {'asset': item['a'],
                            'free': item['f'],
                            'locked': item['l']}
                unicorn_fied_data['balances'] += [new_item]
        elif stream_data['data']['e'] == 'balanceUpdate':
            unicorn_fied_data = {'stream_type': '!userData@arr',
                                 'event_type': stream_data['data']['e'],
                                 'event_time': stream_data['data']['E'],
                                 'asset': stream_data['data']['a'],
                                 'balance_delta': stream_data['data']['d'],
                                 'clear_time': stream_data['data']['T']}
        elif stream_data['data']['e'] == 'executionReport':
            unicorn_fied_data = {'stream_type': '!userData@arr',
                                 'event_type': stream_data['data']['e'],
                                 'event_time': stream_data['data']['E'],
                                 'symbol': stream_data['data']['s'],
                                 'client_order_id': stream_data['data']['c'],
                                 'side': stream_data['data']['S'],
                                 'order_type': stream_data['data']['o'],
                                 'time_in_force': stream_data['data']['f'],
                                 'order_quantity': stream_data['data']['q'],
                                 'order_price': stream_data['data']['p'],
                                 'stop_price': stream_data['data']['P'],
                                 'iceberg_quantity': stream_data['data']['F'],
                                 'ignore_g': stream_data['data']['g'],
                                 'original_client_order_id': stream_data['data']['C'],
                                 'current_execution_type': stream_data['data']['x'],
                                 'current_order_status': stream_data['data']['X'],
                                 'order_reject_reason': stream_data['data']['r'],
                                 'order_id': stream_data['data']['i'],
                                 'last_executed_quantity': stream_data['data']['l'],
                                 'cumulative_filled_quantity': stream_data['data']['z'],
                                 'last_executed_price': stream_data['data']['L'],
                                 'commission_amount': stream_data['data']['n'],
                                 'commission_asset': stream_data['data']['N'],
                                 'transaction_time': stream_data['data']['T'],
                                 'trade_id': stream_data['data']['t'],
                                 'ignore_I': stream_data['data']['I'],
                                 'is_order_working': stream_data['data']['w'],
                                 'is_trade_maker_side': stream_data['data']['m'],
                                 'ignore_M': stream_data['data']['M'],
                                 'order_creation_time': stream_data['data']['O'],
                                 'cumulative_quote_asset_transacted_quantity': stream_data['data']['Z'],
                                 'last_quote_asset_transacted_quantity': stream_data['data']['Y']}
        unicorn_fied_version = [exchange, UnicornFy.VERSION]
        unicorn_fied_data['unicorn_fied'] = unicorn_fied_version
        logger.debug("UnicornFy->binance_com_futures_websocket(" + str(unicorn_fied_data) + ")")
        return unicorn_fied_data

    @staticmethod
    def binance_futures_websocket(stream_data_json, exchange="binance.com-futures", show_deprecated_warning=False):
        """
        unicorn_fy binance.com-futures raw_stream_data

        :param stream_data_json: The received raw stream data from the Binance websocket
        :type stream_data_json: json

        :param exchange: Exchange endpoint.
        :type exchange: str

        :param show_deprecated_warning: Show or hide warning
        :type show_deprecated_warning: bool

        :return: dict
        """
        unicorn_fied_data = False

        logger.debug("UnicornFy->binance_futures_websocket(" + str(stream_data_json) + ")")
        if show_deprecated_warning is True:
            pass
        if UnicornFy.is_json(stream_data_json) is False:
            return stream_data_json

        stream_data = json.loads(stream_data_json)

        try:
            if stream_data['e'] == 'outboundAccountInfo':
                stream_data = {'data': stream_data}
            elif stream_data['e'] == 'executionReport':
                stream_data = {'data': stream_data}
            elif stream_data['e'] == 'balanceUpdate':
                stream_data = {'data': stream_data}
            elif stream_data['e'] == 'ORDER_TRADE_UPDATE':
                stream_data = {'data': stream_data}
            elif stream_data['e'] == 'ACCOUNT_UPDATE':
                stream_data = {'data': stream_data}
            elif stream_data['e'] == 'ACCOUNT_CONFIG_UPDATE':
                stream_data = {'data': stream_data}
            elif stream_data['e'] == 'MARGIN_CALL':
                stream_data = {'data': stream_data}
        except KeyError:
            pass
        try:
            if stream_data['stream'].find('@depth5') != -1:
                stream_data['data']['e'] = "depth"
                stream_data['data']['depth_level'] = 5
            elif stream_data['stream'].find('@depth10') != -1:
                stream_data['data']['e'] = "depth"
                stream_data['data']['depth_level'] = 10
            elif stream_data['stream'].find('@depth20') != -1:
                stream_data['data']['e'] = "depth"
                stream_data['data']['depth_level'] = 20
            elif "@bookTicker" in stream_data['stream']:
                stream_data['data']['e'] = "bookTicker"
        except KeyError:
            pass

        try:
            # return if already unicorn_fied
            if stream_data['unicorn_fied']:
                return stream_data
        except KeyError:
            pass

        try:
            if stream_data['result'] is None:
                unicorn_fied_version = [exchange, UnicornFy.VERSION]
                stream_data['unicorn_fied'] = unicorn_fied_version
                logger.debug(f"UnicornFy->binance_futures_websocket({str(stream_data)}, {str(exchange)}")
                return stream_data
            else:
                unicorn_fied_version = [exchange, UnicornFy.VERSION]
                stream_data['unicorn_fied'] = unicorn_fied_version
                logger.debug(f"UnicornFy->binance_futures_websocket({str(stream_data)}, {str(exchange)}")
                return stream_data
        except KeyError:
            pass

        try:
            if stream_data['error']:
                unicorn_fied_version = [exchange, UnicornFy.VERSION]
                stream_data['unicorn_fied'] = unicorn_fied_version
                logger.debug(f"UnicornFy->binance_futures_websocket({str(stream_data)}, {str(exchange)}")
                return stream_data
        except KeyError:
            pass

        try:
            if stream_data['data']['e'] == 'aggTrade':
                unicorn_fied_data = {'stream_type': stream_data['stream'],
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'symbol': stream_data['data']['s'],
                                     'aggregate_trade_id': stream_data['data']['a'],
                                     'price': stream_data['data']['p'],
                                     'quantity': stream_data['data']['q'],
                                     'first_trade_id': stream_data['data']['f'],
                                     'last_trade_id': stream_data['data']['l'],
                                     'trade_time': stream_data['data']['T'],
                                     'is_market_maker': stream_data['data']['m']}
            elif stream_data['data']['e'] == 'trade':
                # Todo: KeyError: 'b'
                # 'buyer_order_id': stream_data['data']['b'],
                # Todo: KeyError: 'a'
                # 'seller_order_id': stream_data['data']['a'],
                # Todo: KeyError: 'M'
                # , 'ignore': stream_data['data']['M']
                unicorn_fied_data = {'stream_type': stream_data['stream'],
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'symbol': stream_data['data']['s'],
                                     'trade_id': stream_data['data']['t'],
                                     'price': stream_data['data']['p'],
                                     'quantity': stream_data['data']['q'],
                                     'trade_time': stream_data['data']['T'],
                                     'is_market_maker': stream_data['data']['m']}
            elif stream_data['data']['e'] == 'kline':
                stream_data['data'] = UnicornFy.set_to_false_if_not_exist(stream_data['data'], 'f')
                stream_data['data'] = UnicornFy.set_to_false_if_not_exist(stream_data['data'], 'L')
                unicorn_fied_data = {'stream_type': stream_data['stream'],
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'symbol': stream_data['data']['s'],
                                     'kline': {'kline_start_time': stream_data['data']['k']['t'],
                                               'kline_close_time': stream_data['data']['k']['T'],
                                               'symbol': stream_data['data']['k']['s'],
                                               'interval': stream_data['data']['k']['i'],
                                               'first_trade_id': stream_data['data']['f'],
                                               'last_trade_id': stream_data['data']['L'],
                                               'open_price': stream_data['data']['k']['o'],
                                               'close_price': stream_data['data']['k']['c'],
                                               'high_price': stream_data['data']['k']['h'],
                                               'low_price': stream_data['data']['k']['l'],
                                               'base_volume': stream_data['data']['k']['v'],
                                               'number_of_trades': stream_data['data']['k']['n'],
                                               'is_closed': stream_data['data']['k']['x'],
                                               'quote': stream_data['data']['k']['q'],
                                               'taker_by_base_asset_volume': stream_data['data']['k']['V'],
                                               'taker_by_quote_asset_volume': stream_data['data']['k']['Q'],
                                               'ignore': stream_data['data']['k']['B']}}
            elif stream_data['data']['e'] == '24hrMiniTicker':
                try:
                    if stream_data['stream']:
                        pass
                except KeyError:
                    stream_data['stream'] = '!miniTicker@arr'
                unicorn_fied_data = {'stream_type': stream_data['stream'],
                                     'event_type': stream_data['data']['e'],
                                     'data': []}

                try:
                    for item in stream_data['items']:
                        data = {'stream_type': stream_data['stream'],
                                'event_type': item['e'],
                                'event_time': item['E'],
                                'symbol': item['s'],
                                'close_price': item['c'],
                                'open_price': item['o'],
                                'high_price': item['h'],
                                'low_price': item['l'],
                                'taker_by_base_asset_volume': item['v'],
                                'taker_by_quote_asset_volume': item['q']}
                        unicorn_fied_data['data'].append(data)
                except KeyError:
                    data = {'stream_type': stream_data['stream'],
                            'event_type': stream_data['data']['e'],
                            'event_time': stream_data['data']['E'],
                            'symbol': stream_data['data']['s'],
                            'close_price': stream_data['data']['c'],
                            'open_price': stream_data['data']['o'],
                            'high_price': stream_data['data']['h'],
                            'low_price': stream_data['data']['l'],
                            'taker_by_base_asset_volume': stream_data['data']['v'],
                            'taker_by_quote_asset_volume': stream_data['data']['q']}
                    unicorn_fied_data['data'].append(data)
            elif stream_data['data']['e'] == '24hrTicker':
                try:
                    if stream_data['stream']:
                        pass
                except KeyError:
                    stream_data['stream'] = '!ticker@arr'
                unicorn_fied_data = {'stream_type': stream_data['stream'],
                                     'event_type': stream_data['data']['e'],
                                     'data': []}
                try:
                    for item in stream_data['items']:
                        data = {'stream_type': stream_data['stream'],
                                'event_type': item['e'],
                                'event_time': item['E'],
                                'symbol': item['s'],
                                'price_change': item['p'],
                                'price_change_percent': item['P'],
                                'weighted_average_price': item['w'],
                                'trade_before_24h_window': item['x'],
                                'last_price': item['c'],
                                'last_quantity': item['Q'],
                                'best_bid_price': item['b'],
                                'best_bid_quantity': item['B'],
                                'best_ask_price': item['a'],
                                'best_ask_quantity': item['A'],
                                'open_price': item['o'],
                                'high_price': item['h'],
                                'low_price': item['l'],
                                'total_traded_base_asset_volume': item['v'],
                                'total_traded_quote_asset_volume': item['q'],
                                'statistics_open_time': item['O'],
                                'statistics_close_time': item['C'],
                                'first_trade_id': item['F'],
                                'last_trade_id': item['L'],
                                'total_nr_of_trades': item['n']}
                        unicorn_fied_data['data'].append(data)
                except KeyError:
                    # Todo: KeyError: 'x'
                    # 'trade_before_24h_window': stream_data['data']['x'],
                    # Todo: KeyError: 'b'
                    # 'best_bid_price': stream_data['data']['b'],
                    # Todo: KeyError: 'B'
                    # 'best_bid_quantity': stream_data['data']['B'],
                    # Todo KeyError: 'a'
                    # 'best_ask_price': stream_data['data']['a'],
                    # Todo KeyError: 'A'
                    # 'best_ask_quantity': stream_data['data']['A'],
                    data = {'stream_type': stream_data['stream'],
                            'event_type': stream_data['data']['e'],
                            'event_time': stream_data['data']['E'],
                            'symbol': stream_data['data']['s'],
                            'price_change': stream_data['data']['p'],
                            'price_change_percent': stream_data['data']['P'],
                            'weighted_average_price': stream_data['data']['w'],
                            'last_price': stream_data['data']['c'],
                            'last_quantity': stream_data['data']['Q'],
                            'open_price': stream_data['data']['o'],
                            'high_price': stream_data['data']['h'],
                            'low_price': stream_data['data']['l'],
                            'total_traded_base_asset_volume': stream_data['data']['v'],
                            'total_traded_quote_asset_volume': stream_data['data']['q'],
                            'statistics_open_time': stream_data['data']['O'],
                            'statistics_close_time': stream_data['data']['C'],
                            'first_trade_id': stream_data['data']['F'],
                            'last_trade_id': stream_data['data']['L'],
                            'total_nr_of_trades': stream_data['data']['n']}
                    unicorn_fied_data['data'].append(data)
            elif stream_data['data']['e'] == 'depth':
                # Todo: KeyError: 'lastUpdateId'
                # 'last_update_id': stream_data['data']['lastUpdateId'],
                unicorn_fied_data = {'stream_type': stream_data['stream'],
                                     'event_type': stream_data['data']['e'],
                                     'symbol': stream_data['stream'][:stream_data['stream'].find('@')].upper()}
            elif stream_data['data']['e'] == 'depthUpdate':
                unicorn_fied_data = {'stream_type': stream_data['stream'],
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'symbol': stream_data['data']['s'],
                                     'first_update_id_in_event': stream_data['data']['U'],
                                     'final_update_id_in_event': stream_data['data']['u'],
                                     'bids': stream_data['data']['b'],
                                     'asks': stream_data['data']['a']}
            elif stream_data['data']['e'] == 'outboundAccountInfo':
                unicorn_fied_data = {'stream_type': '!userData@arr',
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'maker_commission_rate': stream_data['data']['m'],
                                     'taker_commission_rate': stream_data['data']['t'],
                                     'buyer_commission_rate': stream_data['data']['b'],
                                     'seller_commission_rate': stream_data['data']['s'],
                                     'can_trade': stream_data['data']['T'],
                                     'can_withdraw': stream_data['data']['W'],
                                     'can_deposit': stream_data['data']['D'],
                                     'balances': []}
                for item in stream_data['data']['B']:
                    new_item = {'asset': item['a'],
                                'free': item['f'],
                                'locked': item['l']}
                    unicorn_fied_data['balances'] += [new_item]
            elif stream_data['data']['e'] == 'balanceUpdate':
                unicorn_fied_data = {'stream_type': '!userData@arr',
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'asset': stream_data['data']['a'],
                                     'balance_delta': stream_data['data']['d'],
                                     'clear_time': stream_data['data']['T']}
            elif stream_data['data']['e'] == 'executionReport':
                unicorn_fied_data = {'stream_type': '!userData@arr',
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'symbol': stream_data['data']['s'],
                                     'client_order_id': stream_data['data']['c'],
                                     'side': stream_data['data']['S'],
                                     'order_type': stream_data['data']['o'],
                                     'time_in_force': stream_data['data']['f'],
                                     'order_quantity': stream_data['data']['q'],
                                     'order_price': stream_data['data']['p'],
                                     'stop_price': stream_data['data']['P'],
                                     'iceberg_quantity': stream_data['data']['F'],
                                     'ignore_g': stream_data['data']['g'],
                                     'original_client_order_id': stream_data['data']['C'],
                                     'current_execution_type': stream_data['data']['x'],
                                     'current_order_status': stream_data['data']['X'],
                                     'order_reject_reason': stream_data['data']['r'],
                                     'order_id': stream_data['data']['i'],
                                     'last_executed_quantity': stream_data['data']['l'],
                                     'cumulative_filled_quantity': stream_data['data']['z'],
                                     'last_executed_price': stream_data['data']['L'],
                                     'commission_amount': stream_data['data']['n'],
                                     'commission_asset': stream_data['data']['N'],
                                     'transaction_time': stream_data['data']['T'],
                                     'trade_id': stream_data['data']['t'],
                                     'ignore_I': stream_data['data']['I'],
                                     'is_order_working': stream_data['data']['w'],
                                     'is_trade_maker_side': stream_data['data']['m'],
                                     'ignore_M': stream_data['data']['M'],
                                     'order_creation_time': stream_data['data']['O'],
                                     'cumulative_quote_asset_transacted_quantity': stream_data['data']['Z'],
                                     'last_quote_asset_transacted_quantity': stream_data['data']['Y']}
            elif stream_data['data']['e'] == 'ORDER_TRADE_UPDATE':
                '''
                    url: https://binance-docs.github.io/apidocs/futures/en/#event-order-update
                    ex:
                    {
                        "e":"ORDER_TRADE_UPDATE",     // Event Type
                        "E":1568879465651,            // Event Time
                        "T":1568879465650,            // Transaction Time
                        "o":{                             
                                "s":"BTCUSDT",              // Symbol
                                "c":"TEST",                 // Client Order Id
                                // special client order id:
                                // starts with "autoclose-": liquidation order
                                // "adl_autoclose": ADL auto close order
                                "S":"SELL",                 // Side
                                "o":"TRAILING_STOP_MARKET", // Order Type
                                "f":"GTC",                  // Time in Force
                                "q":"0.001",                // Original Quantity
                                "p":"0",                    // Original Price
                                "ap":"0",                   // Average Price
                                "sp":"7103.04",             // Stop Price. Please ignore with TRAILING_STOP_MARKET order
                                "x":"NEW",                  // Execution Type
                                "X":"NEW",                  // Order Status
                                "i":8886774,                // Order Id
                                "l":"0",                    // Order Last Filled Quantity
                                "z":"0",                    // Order Filled Accumulated Quantity
                                "L":"0",                    // Last Filled Price
                                "N":"USDT",             // Commission Asset, will not push if no commission
                                "n":"0",                // Commission, will not push if no commission
                                "T":1568879465651,          // Order Trade Time
                                "t":0,                      // Trade Id
                                "b":"0",                    // Bids Notional
                                "a":"9.91",                 // Ask Notional
                                "m":false,                  // Is this trade the maker side?
                                "R":false,                  // Is this reduce only
                                "wt":"CONTRACT_PRICE",      // Stop Price Working Type
                                "ot":"TRAILING_STOP_MARKET",    // Original Order Type
                                "ps":"LONG",                        // Position Side
                                "cp":false,                     // If Close-All, pushed with conditional order
                                "AP":"7476.89",             // Activation Price, only puhed with TRAILING_STOP_MARKET order
                                "cr":"5.0",                 // Callback Rate, only puhed with TRAILING_STOP_MARKET order
                                "rp":"0"                            // Realized Profit of the trade
                            }
                        }
                '''
                unicorn_fied_data = {'stream_type': 'ORDER_TRADE_UPDATE',
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'symbol': stream_data['data']['o']['s'],  # Symbol
                                     'client_order_id': stream_data['data']['o']['c'],  # Client Order Id
                                     'side': stream_data['data']['o']['S'],  # Side
                                     'order_type': stream_data['data']['o']['o'],  # Order Type
                                     'time_in_force': stream_data['data']['o']['f'],  # Time in Force
                                     'order_quantity': stream_data['data']['o']['q'],  # Original Quantity
                                     'order_price': stream_data['data']['o']['p'],  # Original Price
                                     'order_avg_price': stream_data['data']['o']['ap'],  # Average Price
                                     'order_stop_price': stream_data['data']['o']['sp'],  # Stop Price.
                                     'current_execution_type': stream_data['data']['o']['x'],  # Execution Type
                                     'current_order_status': stream_data['data']['o']['X'],  # Order Status
                                     'order_id': stream_data['data']['o']['i'],  # Order Id
                                     'last_executed_quantity': stream_data['data']['o']['l'],
                                     'cumulative_filled_quantity': stream_data['data']['o']['z'],
                                     'last_executed_price': stream_data['data']['o']['L'],  # Last Filled Price
                                     'transaction_time': stream_data['data']['o']['T'],  # Order Trade Time
                                     'trade_id': stream_data['data']['o']['t'],  # Trade Id
                                     'net_pay': stream_data['data']['o']['b'],  # Ask Notional
                                     'net_selling_order_value': stream_data['data']['o']['a'],  # Ask Notional
                                     'is_trade_maker_side': stream_data['data']['o']['m'],
                                     'reduce_only': stream_data['data']['o']['R'],  # Is this reduce only
                                     'trigger_price_type': stream_data['data']['o']['wt'],  # Stop Price Working Type
                                     'order_price_type': stream_data['data']['o']['ot'],  # Original Order Type
                                     'position_side': stream_data['data']['o']['ps'],
                                     # Todo:
                                     # 'cumulative_quote_asset_transacted_quantity': stream_data['data']['cp'],
                                     # 'cumulative_quote_asset_transacted_quantity': stream_data['data']['AP'],
                                     # 'cumulative_quote_asset_transacted_quantity': stream_data['data']['cr'],
                                     'order_realized_profit': stream_data['data']['o']['rp']}  # Realized Profit
            elif stream_data['data']['e'] == 'ACCOUNT_UPDATE':
                '''
                    url: https://binance-docs.github.io/apidocs/futures/en/#event-balance-and-position-update
                    ex:
                       {
                        "e": "ACCOUNT_UPDATE",                // Event Type
                        "E": 1564745798939,                   // Event Time
                        "T": 1564745798938 ,                  // Transaction
                        "a":                                  // Update Data
                            {
                            "m":"ORDER",                      // Event reason type
                            "B":[                             // Balances
                                {
                                "a":"USDT",                   // Asset
                                "wb":"122624.12345678",       // Wallet Balance
                                "cw":"100.12345678"           // Cross Wallet Balance
                                },
                                {
                                "a":"BNB",           
                                "wb":"1.00000000",
                                "cw":"0.00000000"         
                                }
                            ],
                            "P":[
                                {
                                "s":"BTCUSDT",            // Symbol
                                "pa":"0",                 // Position Amount
                                "ep":"0.00000",            // Entry Price
                                "cr":"200",               // (Pre-fee) Accumulated Realized
                                "up":"0",                     // Unrealized PnL
                                "mt":"isolated",              // Margin Type
                                "iw":"0.00000000",            // Isolated Wallet (if isolated position)
                                "ps":"BOTH"                   // Position Side
                                }，
                                {
                                    "s":"BTCUSDT",
                                    "pa":"20",
                                    "ep":"6563.66500",
                                    "cr":"0",
                                    "up":"2850.21200",
                                    "mt":"isolated",
                                    "iw":"13200.70726908",
                                    "ps":"LONG"
                                },
                                {
                                    "s":"BTCUSDT",
                                    "pa":"-10",
                                    "ep":"6563.86000",
                                    "cr":"-45.04000000",
                                    "up":"-1423.15600",
                                    "mt":"isolated",
                                    "iw":"6570.42511771",
                                    "ps":"SHORT"
                                }
                            ]
                            }
                        } 
                '''
                unicorn_fied_data = {
                    'stream_type': 'ACCOUNT_UPDATE',
                    'event_type': stream_data['data']['e'],
                    'event_time': stream_data['data']['E'],
                    'transaction': stream_data['data']['T'],
                    'event_reason': stream_data['data']['a']['m'],
                    'balances': [],
                    'positions': []
                }

                for balance in stream_data['data']['a']['B']:
                    unicorn_fied_data['balances'].append({
                        'asset': balance['a'],
                        'wallet_balance': balance['wb'],
                        'cross_wallet_balance': balance['cw']
                    })

                for position in stream_data['data']['a']['P']:
                    unicorn_fied_data['positions'].append({
                        'symbol': position['s'],
                        'position_amount': position['pa'],
                        'entry_price': position['ep'],
                        'accumulated_realized': position['cr'],
                        'upnl': position['up'],
                        'margin_type': position['mt'],
                        'isolated_wallet': position['iw'],
                        'position_side': position['ps']
                    })
            elif stream_data['data']['e'] == 'MARGIN_CALL':
                '''
                    url: https://binance-docs.github.io/apidocs/futures/en/#event-margin-call
                    ex: {
                            "e":"MARGIN_CALL",      // Event Type
                            "E":1587727187525,      // Event Time
                            "cw":"3.16812045",      // Cross Wallet Balance. Only pushed with crossed position margin call
                            "p":[                   // Position(s) of Margin Call
                            {
                                "s":"ETHUSDT",      // Symbol
                                "ps":"LONG",        // Position Side
                                "pa":"1.327",       // Position Amount
                                "mt":"CROSSED",     // Margin Type
                                "iw":"0",           // Isolated Wallet (if isolated position)
                                "mp":"187.17127",   // Mark Price
                                "up":"-1.166074",   // Unrealized PnL
                                "mm":"1m,n.614445"     // Maintenance Margin Required
                            }
                            ]
                        }  
                '''
                unicorn_fied_data = {'stream_type': 'MARGIN_CALL',
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'symbol': stream_data['data']['p']['s'],
                                     'side': stream_data['data']['p']['ps'],
                                     'amount': stream_data['data']['p']['pa'],
                                     'type': stream_data['data']['p']['mt'],
                                     'wallet': stream_data['data']['p']['iw'],
                                     'price': stream_data['data']['p']['mp'],
                                     'pnl': stream_data['data']['p']['up'],
                                     'margin': stream_data['data']['p']['mm']}
            elif stream_data['data']['e'] == 'ACCOUNT_CONFIG_UPDATE':
                '''
                url: https://binance-docs.github.io/apidocs/futures/en/#event-order-update
                ex:
                {
                    "e":"ACCOUNT_CONFIG_UPDATE",       // Event Type
                    "E":1611646737479,                 // Event Time
                    "T":1611646737476,                 // Transaction Time
                    "ac":{                              
                    "s":"BTCUSDT",                     // symbol
                    "l":25                             // leverage
                    }
                }  
                '''
                unicorn_fied_data = {'stream_type': 'ACCOUNT_CONFIG_UPDATE',
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'symbol': stream_data['data']['ac']['s'],
                                     'leverage': stream_data['data']['ac']['l']
                                     }
        except TypeError as error_msg:
            logger.critical(f"UnicornFy->binance_futures_websocket({str(unicorn_fied_data)}) - "
                            f"error: {str(error_msg)}")
        unicorn_fied_version = [exchange, UnicornFy.VERSION]
        try:
            unicorn_fied_data['unicorn_fied'] = unicorn_fied_version
        except TypeError as error_msg:
            logger.critical(f"UnicornFy->binance_futures_websocket({str(unicorn_fied_data)}) - "
                            f"error: {str(error_msg)}")
        logger.debug("UnicornFy->binance_futures_websocket(" + str(unicorn_fied_data) + ")")
        return unicorn_fied_data

    @staticmethod
    def binance_coin_futures_websocket(stream_data_json, exchange="binance.com-coin_futures",
                                       show_deprecated_warning=False):
        """
        unicorn_fy binance.com-coin_futures raw_stream_data

        :param stream_data_json: The received raw stream data from the Binance websocket
        :type stream_data_json: json

        :param exchange: Exchange endpoint.
        :type exchange: str

        :param show_deprecated_warning: Show or hide warning
        :type show_deprecated_warning: bool

        :return: dict
        """
        unicorn_fied_data = False

        logger.debug("UnicornFy->binance_coin_futures_websocket(" + str(stream_data_json) + ")")
        if show_deprecated_warning is True:
            pass

        if UnicornFy.is_json(stream_data_json) is False:
            return stream_data_json

        stream_data = json.loads(stream_data_json)

        try:
            if stream_data['e'] == 'outboundAccountInfo':
                stream_data = {'data': stream_data}
            elif stream_data['e'] == 'executionReport':
                stream_data = {'data': stream_data}
            elif stream_data['e'] == 'balanceUpdate':
                stream_data = {'data': stream_data}
            elif stream_data['e'] == 'ORDER_TRADE_UPDATE':
                stream_data = {'data': stream_data}
            elif stream_data['e'] == 'ACCOUNT_UPDATE':
                stream_data = {'data': stream_data}
            elif stream_data['e'] == 'ACCOUNT_CONFIG_UPDATE':
                stream_data = {'data': stream_data}
            elif stream_data['e'] == 'MARGIN_CALL':
                stream_data = {'data': stream_data}
        except KeyError:
            pass
        try:
            if stream_data['stream'].find('@depth5') != -1:
                stream_data['data']['e'] = "depth"
                stream_data['data']['depth_level'] = 5
            elif stream_data['stream'].find('@depth10') != -1:
                stream_data['data']['e'] = "depth"
                stream_data['data']['depth_level'] = 10
            elif stream_data['stream'].find('@depth20') != -1:
                stream_data['data']['e'] = "depth"
                stream_data['data']['depth_level'] = 20
            elif "@bookTicker" in stream_data['stream']:
                stream_data['data']['e'] = "bookTicker"
        except KeyError:
            pass

        try:
            # return if already unicorn_fied
            if stream_data['unicorn_fied']:
                return stream_data
        except KeyError:
            pass

        try:
            if stream_data['result'] is None:
                unicorn_fied_version = [exchange, UnicornFy.VERSION]
                stream_data['unicorn_fied'] = unicorn_fied_version
                logger.debug(f"UnicornFy->binance_coin_futures_websocket({str(stream_data)}, {str(exchange)}")
                return stream_data
            else:
                unicorn_fied_version = [exchange, UnicornFy.VERSION]
                stream_data['unicorn_fied'] = unicorn_fied_version
                logger.debug(f"UnicornFy->binance_coin_futures_websocket({str(stream_data)}, {str(exchange)}")
                return stream_data
        except KeyError:
            pass

        try:
            if stream_data['error']:
                unicorn_fied_version = [exchange, UnicornFy.VERSION]
                stream_data['unicorn_fied'] = unicorn_fied_version
                logger.debug(f"UnicornFy->binance_coin_futures_websocket({str(stream_data)}, {str(exchange)}")
                return stream_data
        except KeyError:
            pass

        try:
            if stream_data['data']['e'] == 'aggTrade':
                unicorn_fied_data = {'stream_type': stream_data['stream'],
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'symbol': stream_data['data']['s'],
                                     'aggregate_trade_id': stream_data['data']['a'],
                                     'price': stream_data['data']['p'],
                                     'quantity': stream_data['data']['q'],
                                     'first_trade_id': stream_data['data']['f'],
                                     'last_trade_id': stream_data['data']['l'],
                                     'trade_time': stream_data['data']['T'],
                                     'is_market_maker': stream_data['data']['m']}
            elif stream_data['data']['e'] == 'trade':
                # Todo: KeyError: 'b'
                # 'buyer_order_id': stream_data['data']['b'],
                # Todo: KeyError: 'a'
                # 'seller_order_id': stream_data['data']['a'],
                # Todo: KeyError: 'M'
                # , 'ignore': stream_data['data']['M']
                unicorn_fied_data = {'stream_type': stream_data['stream'],
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'symbol': stream_data['data']['s'],
                                     'trade_id': stream_data['data']['t'],
                                     'price': stream_data['data']['p'],
                                     'quantity': stream_data['data']['q'],
                                     'trade_time': stream_data['data']['T'],
                                     'is_market_maker': stream_data['data']['m']}
            elif stream_data['data']['e'] == 'kline':
                stream_data['data'] = UnicornFy.set_to_false_if_not_exist(stream_data['data'], 'f')
                stream_data['data'] = UnicornFy.set_to_false_if_not_exist(stream_data['data'], 'L')
                unicorn_fied_data = {'stream_type': stream_data['stream'],
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'symbol': stream_data['data']['s'],
                                     'kline': {'kline_start_time': stream_data['data']['k']['t'],
                                               'kline_close_time': stream_data['data']['k']['T'],
                                               'symbol': stream_data['data']['k']['s'],
                                               'interval': stream_data['data']['k']['i'],
                                               'first_trade_id': stream_data['data']['f'],
                                               'last_trade_id': stream_data['data']['L'],
                                               'open_price': stream_data['data']['k']['o'],
                                               'close_price': stream_data['data']['k']['c'],
                                               'high_price': stream_data['data']['k']['h'],
                                               'low_price': stream_data['data']['k']['l'],
                                               'base_volume': stream_data['data']['k']['v'],
                                               'number_of_trades': stream_data['data']['k']['n'],
                                               'is_closed': stream_data['data']['k']['x'],
                                               'quote': stream_data['data']['k']['q'],
                                               'taker_by_base_asset_volume': stream_data['data']['k']['V'],
                                               'taker_by_quote_asset_volume': stream_data['data']['k']['Q'],
                                               'ignore': stream_data['data']['k']['B']}}
            elif stream_data['data']['e'] == '24hrMiniTicker':
                try:
                    if stream_data['stream']:
                        pass
                except KeyError:
                    stream_data['stream'] = '!miniTicker@arr'
                unicorn_fied_data = {'stream_type': stream_data['stream'],
                                     'event_type': stream_data['data']['e'],
                                     'data': []}

                try:
                    for item in stream_data['items']:
                        data = {'stream_type': stream_data['stream'],
                                'event_type': item['e'],
                                'event_time': item['E'],
                                'symbol': item['s'],
                                'close_price': item['c'],
                                'open_price': item['o'],
                                'high_price': item['h'],
                                'low_price': item['l'],
                                'taker_by_base_asset_volume': item['v'],
                                'taker_by_quote_asset_volume': item['q']}
                        unicorn_fied_data['data'].append(data)
                except KeyError:
                    data = {'stream_type': stream_data['stream'],
                            'event_type': stream_data['data']['e'],
                            'event_time': stream_data['data']['E'],
                            'symbol': stream_data['data']['s'],
                            'close_price': stream_data['data']['c'],
                            'open_price': stream_data['data']['o'],
                            'high_price': stream_data['data']['h'],
                            'low_price': stream_data['data']['l'],
                            'taker_by_base_asset_volume': stream_data['data']['v'],
                            'taker_by_quote_asset_volume': stream_data['data']['q']}
                    unicorn_fied_data['data'].append(data)
            elif stream_data['data']['e'] == '24hrTicker':
                try:
                    if stream_data['stream']:
                        pass
                except KeyError:
                    stream_data['stream'] = '!ticker@arr'
                unicorn_fied_data = {'stream_type': stream_data['stream'],
                                     'event_type': stream_data['data']['e'],
                                     'data': []}
                try:
                    for item in stream_data['items']:
                        data = {'stream_type': stream_data['stream'],
                                'event_type': item['e'],
                                'event_time': item['E'],
                                'symbol': item['s'],
                                'price_change': item['p'],
                                'price_change_percent': item['P'],
                                'weighted_average_price': item['w'],
                                'trade_before_24h_window': item['x'],
                                'last_price': item['c'],
                                'last_quantity': item['Q'],
                                'best_bid_price': item['b'],
                                'best_bid_quantity': item['B'],
                                'best_ask_price': item['a'],
                                'best_ask_quantity': item['A'],
                                'open_price': item['o'],
                                'high_price': item['h'],
                                'low_price': item['l'],
                                'total_traded_base_asset_volume': item['v'],
                                'total_traded_quote_asset_volume': item['q'],
                                'statistics_open_time': item['O'],
                                'statistics_close_time': item['C'],
                                'first_trade_id': item['F'],
                                'last_trade_id': item['L'],
                                'total_nr_of_trades': item['n']}
                        unicorn_fied_data['data'].append(data)
                except KeyError:
                    # Todo: KeyError: 'x'
                    # 'trade_before_24h_window': stream_data['data']['x'],
                    # Todo: KeyError: 'b'
                    # 'best_bid_price': stream_data['data']['b'],
                    # Todo: KeyError: 'B'
                    # 'best_bid_quantity': stream_data['data']['B'],
                    # Todo KeyError: 'a'
                    # 'best_ask_price': stream_data['data']['a'],
                    # Todo KeyError: 'A'
                    # 'best_ask_quantity': stream_data['data']['A'],
                    data = {'stream_type': stream_data['stream'],
                            'event_type': stream_data['data']['e'],
                            'event_time': stream_data['data']['E'],
                            'symbol': stream_data['data']['s'],
                            'price_change': stream_data['data']['p'],
                            'price_change_percent': stream_data['data']['P'],
                            'weighted_average_price': stream_data['data']['w'],
                            'last_price': stream_data['data']['c'],
                            'last_quantity': stream_data['data']['Q'],
                            'open_price': stream_data['data']['o'],
                            'high_price': stream_data['data']['h'],
                            'low_price': stream_data['data']['l'],
                            'total_traded_base_asset_volume': stream_data['data']['v'],
                            'total_traded_quote_asset_volume': stream_data['data']['q'],
                            'statistics_open_time': stream_data['data']['O'],
                            'statistics_close_time': stream_data['data']['C'],
                            'first_trade_id': stream_data['data']['F'],
                            'last_trade_id': stream_data['data']['L'],
                            'total_nr_of_trades': stream_data['data']['n']}
                    unicorn_fied_data['data'].append(data)
            elif stream_data['data']['e'] == 'depth':
                # Todo: KeyError: 'lastUpdateId'
                # 'last_update_id': stream_data['data']['lastUpdateId'],
                # Todo: KeyError: 'bids'
                # 'bids': stream_data['data']['bids'],
                # , 'asks': stream_data['data']['asks']
                unicorn_fied_data = {'stream_type': stream_data['stream'],
                                     'event_type': stream_data['data']['e'],
                                     'symbol': stream_data['stream'][:stream_data['stream'].find('@')].upper()}
            elif stream_data['data']['e'] == 'depthUpdate':
                # Todo: KeyError: 'bids'
                # 'bids': stream_data['data']['b'],
                unicorn_fied_data = {'stream_type': stream_data['stream'],
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'symbol': stream_data['data']['s'],
                                     'first_update_id_in_event': stream_data['data']['U'],
                                     'final_update_id_in_event': stream_data['data']['u'],
                                     'asks': stream_data['data']['a']}
            elif stream_data['data']['e'] == 'outboundAccountInfo':
                unicorn_fied_data = {'stream_type': '!userData@arr',
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'maker_commission_rate': stream_data['data']['m'],
                                     'taker_commission_rate': stream_data['data']['t'],
                                     'buyer_commission_rate': stream_data['data']['b'],
                                     'seller_commission_rate': stream_data['data']['s'],
                                     'can_trade': stream_data['data']['T'],
                                     'can_withdraw': stream_data['data']['W'],
                                     'can_deposit': stream_data['data']['D'],
                                     'balances': []}
                for item in stream_data['data']['B']:
                    new_item = {'asset': item['a'],
                                'free': item['f'],
                                'locked': item['l']}
                    unicorn_fied_data['balances'] += [new_item]
            elif stream_data['data']['e'] == 'balanceUpdate':
                unicorn_fied_data = {'stream_type': '!userData@arr',
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'asset': stream_data['data']['a'],
                                     'balance_delta': stream_data['data']['d'],
                                     'clear_time': stream_data['data']['T']}
            elif stream_data['data']['e'] == 'executionReport':
                unicorn_fied_data = {'stream_type': '!userData@arr',
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'symbol': stream_data['data']['s'],
                                     'client_order_id': stream_data['data']['c'],
                                     'side': stream_data['data']['S'],
                                     'order_type': stream_data['data']['o'],
                                     'time_in_force': stream_data['data']['f'],
                                     'order_quantity': stream_data['data']['q'],
                                     'order_price': stream_data['data']['p'],
                                     'stop_price': stream_data['data']['P'],
                                     'iceberg_quantity': stream_data['data']['F'],
                                     'ignore_g': stream_data['data']['g'],
                                     'original_client_order_id': stream_data['data']['C'],
                                     'current_execution_type': stream_data['data']['x'],
                                     'current_order_status': stream_data['data']['X'],
                                     'order_reject_reason': stream_data['data']['r'],
                                     'order_id': stream_data['data']['i'],
                                     'last_executed_quantity': stream_data['data']['l'],
                                     'cumulative_filled_quantity': stream_data['data']['z'],
                                     'last_executed_price': stream_data['data']['L'],
                                     'commission_amount': stream_data['data']['n'],
                                     'commission_asset': stream_data['data']['N'],
                                     'transaction_time': stream_data['data']['T'],
                                     'trade_id': stream_data['data']['t'],
                                     'ignore_I': stream_data['data']['I'],
                                     'is_order_working': stream_data['data']['w'],
                                     'is_trade_maker_side': stream_data['data']['m'],
                                     'ignore_M': stream_data['data']['M'],
                                     'order_creation_time': stream_data['data']['O'],
                                     'cumulative_quote_asset_transacted_quantity': stream_data['data']['Z'],
                                     'last_quote_asset_transacted_quantity': stream_data['data']['Y']}
            elif stream_data['data']['e'] == 'ORDER_TRADE_UPDATE':
                '''
                    url: https://binance-docs.github.io/apidocs/futures/en/#event-order-update
                    ex:
                    {
                        "e":"ORDER_TRADE_UPDATE",     // Event Type
                        "E":1568879465651,            // Event Time
                        "T":1568879465650,            // Transaction Time
                        "o":{                             
                                "s":"BTCUSDT",              // Symbol
                                "c":"TEST",                 // Client Order Id
                                // special client order id:
                                // starts with "autoclose-": liquidation order
                                // "adl_autoclose": ADL auto close order
                                "S":"SELL",                 // Side
                                "o":"TRAILING_STOP_MARKET", // Order Type
                                "f":"GTC",                  // Time in Force
                                "q":"0.001",                // Original Quantity
                                "p":"0",                    // Original Price
                                "ap":"0",                   // Average Price
                                "sp":"7103.04",             // Stop Price. Please ignore with TRAILING_STOP_MARKET order
                                "x":"NEW",                  // Execution Type
                                "X":"NEW",                  // Order Status
                                "i":8886774,                // Order Id
                                "l":"0",                    // Order Last Filled Quantity
                                "z":"0",                    // Order Filled Accumulated Quantity
                                "L":"0",                    // Last Filled Price
                                "N":"USDT",             // Commission Asset, will not push if no commission
                                "n":"0",                // Commission, will not push if no commission
                                "T":1568879465651,          // Order Trade Time
                                "t":0,                      // Trade Id
                                "b":"0",                    // Bids Notional
                                "a":"9.91",                 // Ask Notional
                                "m":false,                  // Is this trade the maker side?
                                "R":false,                  // Is this reduce only
                                "wt":"CONTRACT_PRICE",      // Stop Price Working Type
                                "ot":"TRAILING_STOP_MARKET",    // Original Order Type
                                "ps":"LONG",                        // Position Side
                                "cp":false,                     // If Close-All, pushed with conditional order
                                "AP":"7476.89",             // Activation Price, only puhed with TRAILING_STOP_MARKET order
                                "cr":"5.0",                 // Callback Rate, only puhed with TRAILING_STOP_MARKET order
                                "rp":"0"                            // Realized Profit of the trade
                            }
                        }
                '''
                unicorn_fied_data = {'stream_type': 'ORDER_TRADE_UPDATE',
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'symbol': stream_data['data']['o']['s'],  # Symbol
                                     'client_order_id': stream_data['data']['o']['c'],  # Client Order Id
                                     'side': stream_data['data']['o']['S'],  # Side
                                     'order_type': stream_data['data']['o']['o'],  # Order Type
                                     'time_in_force': stream_data['data']['o']['f'],  # Time in Force
                                     'order_quantity': stream_data['data']['o']['q'],  # Original Quantity
                                     'order_price': stream_data['data']['o']['p'],  # Original Price
                                     'order_avg_price': stream_data['data']['o']['ap'],  # Average Price
                                     'order_stop_price': stream_data['data']['o']['sp'],  # Stop Price.
                                     'current_execution_type': stream_data['data']['o']['x'],  # Execution Type
                                     'current_order_status': stream_data['data']['o']['X'],  # Order Status
                                     'order_id': stream_data['data']['o']['i'],  # Order Id
                                     'last_executed_quantity': stream_data['data']['o']['l'],
                                     'cumulative_filled_quantity': stream_data['data']['o']['z'],
                                     'last_executed_price': stream_data['data']['o']['L'],  # Last Filled Price
                                     'transaction_time': stream_data['data']['o']['T'],  # Order Trade Time
                                     'trade_id': stream_data['data']['o']['t'],  # Trade Id
                                     'net_pay': stream_data['data']['o']['b'],  # Ask Notional
                                     'net_selling_order_value': stream_data['data']['o']['a'],  # Ask Notional
                                     'is_trade_maker_side': stream_data['data']['o']['m'],
                                     'reduce_only': stream_data['data']['o']['R'],  # Is this reduce only
                                     'trigger_price_type': stream_data['data']['o']['wt'],  # Stop Price Working Type
                                     'order_price_type': stream_data['data']['o']['ot'],  # Original Order Type
                                     'position_side': stream_data['data']['o']['ps'],
                                     # Todo:
                                     # 'cumulative_quote_asset_transacted_quantity': stream_data['data']['cp'],
                                     # 'cumulative_quote_asset_transacted_quantity': stream_data['data']['AP'],
                                     # 'cumulative_quote_asset_transacted_quantity': stream_data['data']['cr'],
                                     'order_realized_profit': stream_data['data']['o']['rp']}  # Realized Profit
            elif stream_data['data']['e'] == 'ACCOUNT_UPDATE':
                '''
                    url: https://binance-docs.github.io/apidocs/futures/en/#event-balance-and-position-update
                    ex:
                       {
                        "e": "ACCOUNT_UPDATE",                // Event Type
                        "E": 1564745798939,                   // Event Time
                        "T": 1564745798938 ,                  // Transaction
                        "a":                                  // Update Data
                            {
                            "m":"ORDER",                      // Event reason type
                            "B":[                             // Balances
                                {
                                "a":"USDT",                   // Asset
                                "wb":"122624.12345678",       // Wallet Balance
                                "cw":"100.12345678"           // Cross Wallet Balance
                                },
                                {
                                "a":"BNB",           
                                "wb":"1.00000000",
                                "cw":"0.00000000"         
                                }
                            ],
                            "P":[
                                {
                                "s":"BTCUSDT",            // Symbol
                                "pa":"0",                 // Position Amount
                                "ep":"0.00000",            // Entry Price
                                "cr":"200",               // (Pre-fee) Accumulated Realized
                                "up":"0",                     // Unrealized PnL
                                "mt":"isolated",              // Margin Type
                                "iw":"0.00000000",            // Isolated Wallet (if isolated position)
                                "ps":"BOTH"                   // Position Side
                                }，
                                {
                                    "s":"BTCUSDT",
                                    "pa":"20",
                                    "ep":"6563.66500",
                                    "cr":"0",
                                    "up":"2850.21200",
                                    "mt":"isolated",
                                    "iw":"13200.70726908",
                                    "ps":"LONG"
                                },
                                {
                                    "s":"BTCUSDT",
                                    "pa":"-10",
                                    "ep":"6563.86000",
                                    "cr":"-45.04000000",
                                    "up":"-1423.15600",
                                    "mt":"isolated",
                                    "iw":"6570.42511771",
                                    "ps":"SHORT"
                                }
                            ]
                            }
                        } 
                '''
                # Todo: unfinished!
                unicorn_fied_data = {'stream_type': 'ACCOUNT_UPDATE',
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'transaction': stream_data['data']['T'],
                                     'update_data': stream_data['data']['a']}
            elif stream_data['data']['e'] == 'MARGIN_CALL':
                '''
                    url: https://binance-docs.github.io/apidocs/futures/en/#event-margin-call
                    ex: {
                            "e":"MARGIN_CALL",      // Event Type
                            "E":1587727187525,      // Event Time
                            "cw":"3.16812045",      // Cross Wallet Balance. Only pushed with crossed position margin call
                            "p":[                   // Position(s) of Margin Call
                            {
                                "s":"ETHUSDT",      // Symbol
                                "ps":"LONG",        // Position Side
                                "pa":"1.327",       // Position Amount
                                "mt":"CROSSED",     // Margin Type
                                "iw":"0",           // Isolated Wallet (if isolated position)
                                "mp":"187.17127",   // Mark Price
                                "up":"-1.166074",   // Unrealized PnL
                                "mm":"1m,n.614445"     // Maintenance Margin Required
                            }
                            ]
                        }  
                '''
                unicorn_fied_data = {'stream_type': 'MARGIN_CALL',
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'symbol': stream_data['data']['p']['s'],
                                     'side': stream_data['data']['p']['ps'],
                                     'amount': stream_data['data']['p']['pa'],
                                     'type': stream_data['data']['p']['mt'],
                                     'wallet': stream_data['data']['p']['iw'],
                                     'price': stream_data['data']['p']['mp'],
                                     'pnl': stream_data['data']['p']['up'],
                                     'margin': stream_data['data']['p']['mm']}
            elif stream_data['data']['e'] == 'ACCOUNT_CONFIG_UPDATE':
                '''
                url: https://binance-docs.github.io/apidocs/futures/en/#event-order-update
                ex:
                {
                    "e":"ACCOUNT_CONFIG_UPDATE",       // Event Type
                    "E":1611646737479,                 // Event Time
                    "T":1611646737476,                 // Transaction Time
                    "ac":{                              
                    "s":"BTCUSDT",                     // symbol
                    "l":25                             // leverage
                    }
                }  
                '''
                unicorn_fied_data = {'stream_type': 'ACCOUNT_CONFIG_UPDATE',
                                     'event_type': stream_data['data']['e'],
                                     'event_time': stream_data['data']['E'],
                                     'symbol': stream_data['data']['ac']['s'],
                                     'leverage': stream_data['data']['ac']['l']
                                     }
        except TypeError as error_msg:
            logger.critical(f"UnicornFy->binance_coin_futures_websocket({str(unicorn_fied_data)}) - "
                            f"error: {str(error_msg)}")
        unicorn_fied_version = [exchange, UnicornFy.VERSION]
        try:
            unicorn_fied_data['unicorn_fied'] = unicorn_fied_version
        except TypeError as error_msg:
            logger.critical(f"UnicornFy->binance_coin_futures_websocket({str(unicorn_fied_data)}) - "
                            f"error: {str(error_msg)}")
        logger.debug("UnicornFy->binance_coin_futures_websocket(" + str(unicorn_fied_data) + ")")
        return unicorn_fied_data

    @staticmethod
    def jex_com_websocket(stream_data_json):
        """
        unicorn_fy jex.com raw_stream_data

        :param stream_data_json: The received raw stream data from the Binance websocket
        :type stream_data_json: json

        :return: dict
        """
        return UnicornFy.binance_websocket(stream_data_json, exchange="jex.com", show_deprecated_warning=False)

    @staticmethod
    def get_latest_release_info():
        """
        Get infos about the latest available release

        :return: dict or False
        """
        try:
            respond = requests.get('https://api.github.com/repos/oliver-zehentleitner/unicorn-fy/releases/latest')
            return respond.json()
        except Exception:
            return False

    def get_latest_version(self):
        """
        Get the version of the latest available release (cache time 1 hour)

        :return: str or False
        """
        # Do a fresh request if status is None or last timestamp is older 1 hour
        if self.last_update_check_github['status'] is None or \
                (self.last_update_check_github['timestamp'] + (60 * 60) < time.time()):
            self.last_update_check_github['status'] = self.get_latest_release_info()
        if self.last_update_check_github['status']:
            try:
                return self.last_update_check_github['status']["tag_name"]
            except KeyError:
                return "unknown"
        else:
            return "unknown"

    @staticmethod
    def get_version():
        """
        Get the package/module version

        :return: str
        """
        return UnicornFy.VERSION

    @staticmethod
    def is_json(data):
        """
        Is the string in json format?

        :param data: the data to verify
        :type data: str

        :return: True or False
        :rtype: bool
        """
        try:
            json.loads(data)
        except ValueError:
            return False
        except TypeError:
            return False
        return True

    def is_update_availabe(self):
        """
        Is a new release of this package available?

        :return: bool
        """
        installed_version = self.get_version()
        latest_version = self.get_latest_version()
        if ".dev" in installed_version:
            installed_version = installed_version[:-4]
        if latest_version == installed_version:
            return False
        elif latest_version == "unknown":
            return False
        else:
            return True

    @staticmethod
    def set_to_false_if_not_exist(value, key):
        """
        some vars are non existent if they would be empty, so we create the missing vars with default values

        :param value: default value
        :type value: str

        :param key: the key name
        :type key: str

        :return: final value
        :rtype: str
        """
        try:
            if value[key]:
                return value[key]
        except KeyError:
            value[key] = False
            return value
        except IndexError:
            value[key] = False
            return value
