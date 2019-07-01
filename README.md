![GitHub release](https://img.shields.io/github/release/unicorn-data-analysis/unicorn_fy.svg) 
![GitHub](https://img.shields.io/github/license/unicorn-data-analysis/unicorn_fy.svg?color=blue) 
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/unicorn_fy.svg) 
![PyPI - Status](https://img.shields.io/pypi/status/unicorn_fy.svg) 
![PyPI - yes](https://img.shields.io/badge/PyPI-yes-brightgreen.svg?color=orange) 
![PyPI - Wheel](https://img.shields.io/pypi/wheel/unicorn_fy.svg?label=PyPI%20wheel&color=orange) 
![PyPI - Downloads](https://img.shields.io/pypi/dm/unicorn-fy.svg?label=PyPI%20downloads&color=orange)


# UnicornFy
Unify data from crypto exchanges 
```
from unicorn_fy.unicorn_fy import UnicornFy

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
- binance.com

## Todo
- binance.je (comming soon)
- binance.org (comming soon)
- testnet.binance.org (comming soon)

## Installation
`pip install unicorn-fy`

https://pypi.org/project/unicorn-fy/

## Documentation
https://www.unicorn-data.com/unicorn_fy.html

## Source, Downloads, Examples, ...
https://github.com/unicorn-data-analysis/unicorn_fy

## Wiki
https://github.com/unicorn-data-analysis/unicorn_fy/wiki

## Receive Notifications
To receive notifications on available updates you can ![watch](https://s3.gifyu.com/images/github_watch.png) the 
repository on [GitHub](https://github.com/unicorn-data-analysis/unicorn-binance-websocket-api).

## How to report Bugs or suggest Improvements?
[List of planned features](https://github.com/unicorn-data-analysis/unicorn_fy/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement) - 
click ![thumbs-up](https://s3.gifyu.com/images/tu.png) if you need one of them or suggest a new feature!

Before you report a bug, [try the latest release](https://github.com/unicorn-data-analysis/unicorn_fy#installation). 
If the issue still exists, provide the error trace, OS and python version and explain how to reproduce the error. 
A demo script is appreciated.

If you dont find an issue related to your topic, please open a new issue:
https://github.com/unicorn-data-analysis/unicorn_fy/issues

## Contributing
[unicorn_fy](https://github.com/unicorn-data-analysis/unicorn_fy) is an open 
source project which welcomes contributions which can be anything from simple documentation fixes to new features. To 
contribute, fork the project on [GitHub](https://github.com/unicorn-data-analysis/unicorn_fy) and 
send a pull request. 

We ![love](https://s3.gifyu.com/images/heartae002231c41d8a80.png) open source!