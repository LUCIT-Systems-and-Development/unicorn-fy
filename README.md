![GitHub release](https://img.shields.io/github/release/unicorn-data-analysis/unicorn_fy.svg) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/unicorn-data-analysis/unicorn_fy.svg) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/unicorn_fy.svg) ![PyPI - Status](https://img.shields.io/pypi/status/unicorn_fy.svg) ![PyPI - yes](https://img.shields.io/badge/PyPI-yes-brightgreen.svg) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/unicorn_fy.svg) ![GitHub](https://img.shields.io/github/license/unicorn-data-analysis/unicorn_fy.svg) 

# UnicornFy
Unify data from crypto exchanges
```
received_stream_data_json = {"stream": "btcusdt@trade",
                             "data": {"e": "trade",
                                      "E": 1556876873656,
                                      "s": "BTCUSDT",
                                      "t": 117727701,
                                      "p": "5786.76000000",
                                      "q": "0.03200500",
                                      "b": 341831847,
                                      "a": 341831876,
                                      "T": 1556876873648,
                                      "m": True,
                                      "M": True}}

unicorn_fied_stream_data = UnicornFy.binance_websocket(received_stream_data_json)
print(unicorn_fied_stream_data)
>>>
{'stream_type': 'btcusdt@trade', 'event_type': 'trade', 'event_time': 1556876873656, 'symbol': 'BTCUSDT', 'trade_id': 117727701, 'price': '5786.76000000', 'quantity': '0.03200500', 'buyer_order_id': 341831847, 'seller_order_id': 341831876, 'trade_time': 1556876873648, 'is_market_maker': True, 'ignore': True, 'unicorn_fied': ['binance', '0.1.0']}
```
## Supported Exchanges
- Binance

## Installation
`pip install unicorn-fy`

https://pypi.org/project/unicorn-fy/

## Documentation
https://www.unicorn-data.com/unicorn_fy.html

## Project, code and downloads:
https://github.com/unicorn-data-analysis/unicorn_fy

## Wiki
https://github.com/unicorn-data-analysis/unicorn_fy/wiki

## How to report bugs or suggest improvements?
Please open a new issue:
https://github.com/unicorn-data-analysis/unicorn_fy/issues

If you report a bug, try first the latest release via [download](https://github.com/unicorn-data-analysis/unicorn_fy/releases) 
or with `pip install unicorn-fy --upgrade`. If the issue still exists, provide the error trace, OS 
and python version and explain how to reproduce the error. A demo script is appreciated.

## Contributing
UnicornFy is an open source project which welcomes contributions which can be anything from simple 
documentation fixes to new features. To contribute, fork the project on [GitHub](https://github.com/unicorn-data-analysis/unicorn_fy) and send a pull request.
