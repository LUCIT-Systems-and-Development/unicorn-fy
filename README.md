[![GitHub release](https://img.shields.io/github/release/LUCIT-Systems-and-Development/unicorn-fy.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/releases)
[![GitHub](https://img.shields.io/github/license/LUCIT-Systems-and-Development/unicorn-fy.svg?color=blue)](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/blob/master/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/unicorn_fy.svg)](https://www.python.org/downloads/)
[![Downloads](https://pepy.tech/badge/unicorn-fy)](https://pepy.tech/project/unicorn-fy)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/unicorn_fy.svg?label=PyPI%20wheel)](https://pypi.org/project/unicorn-fy/)
[![PyPI - Status](https://img.shields.io/pypi/status/unicorn_fy.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/issues)
[![Unit Tests](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/actions/workflows/unit-tests.yml)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/LUCIT-Systems-and-Development/unicorn-fy.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/LUCIT-Systems-and-Development/unicorn-fy/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/LUCIT-Systems-and-Development/unicorn-fy.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/LUCIT-Systems-and-Development/unicorn-fy/context:python)
[![codecov](https://codecov.io/gh/LUCIT-Systems-and-Development/unicorn-fy/branch/master/graph/badge.svg?token=5I03AZ3F5S)](https://codecov.io/gh/LUCIT-Systems-and-Development/unicorn-fy)
[![Read the Docs](https://img.shields.io/badge/read-%20docs-yellow)](https://unicorn-fy.docs.lucit.tech/)
[![Github](https://img.shields.io/badge/source-github-yellow)](https://github.com/LUCIT-Systems-and-Development/unicorn-fy)
[![Telegram](https://img.shields.io/badge/chat-telegram-yellow)](https://t.me/unicorndevs)

# UnicornFy
[Supported Exchanges](#supported-exchanges) | [Installation](#installation-and-upgrade) | [Change Log](#change-log) | [Documentation](#documentation) | 
[Examples](#examples) | [Wiki](#wiki) | [Social](#social) | [Notifications](#receive-notifications) | 
[Bugs](#how-to-report-bugs-or-suggest-improvements) | [Contributing](#contributing) | [Commercial Support](#commercial-support)

Convert received raw data from crypto exchange API endpoints into well-formed python dictionaries.

Part of ['UNICORN Binance Suite'](https://www.lucit.tech/unicorn-binance-suite.html).

```
import unicorn_fy

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

unicornfy = unicorn_fy.UnicornFy()

unicorn_fied_stream_data = unicornfy.binance_com_websocket(received_stream_data_json)
print(unicorn_fied_stream_data)
```

Output:

```
{'stream_type': 'btcusdt@trade', 'event_type': 'trade', 'event_time': 1556876873656, 'symbol': 'BTCUSDT',
 'trade_id': 117727701, 'price': '5786.76000000', 'quantity': '0.03200500', 'buyer_order_id': 341831847,
 'seller_order_id': 341831876, 'trade_time': 1556876873648, 'is_market_maker': True, 'ignore': True,
 'unicorn_fied': ['binance', '0.11.1']}
```

This lib is integrated into 
[UNICORN Binance WebSocket API](https://www.lucit.tech/unicorn-binance-websocket-api.html) 
and can be activated by setting parameter 
[`output_default` of `BinanceWebSocketApiManager()` to `UnicornFy`](https://lucit-systems-and-development.github.io/unicorn-binance-websocket-api/unicorn_binance_websocket_api.html?highlight=output_default#module-unicorn_binance_websocket_api.manager) 
or for specific streams with the parameter 
[`output` of `create_stream()` to `UnicornFy`](https://lucit-systems-and-development.github.io/unicorn-binance-websocket-api/unicorn_binance_websocket_api.html?highlight=output#unicorn_binance_websocket_api.manager.BinanceWebSocketApiManager.create_stream).

### Get the right [logger](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/blob/master/example_logging.py):
```
logging.getLogger("unicorn_fy")
```

## Supported Exchanges
### Websockets

| Exchange | Docs            | Status | 
| -------- | --------------- | ------ |
| [Binance](https://www.binance.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_websocket(stream_data_json)`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_websocket) | STABLE |
| [Binance Testnet](https://testnet.binance.vision/) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_websocket(stream_data_json)`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_websocket) | STABLE |
| [Binance Margin](https://www.binance.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_margin_websocket(stream_data_json)`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_margin_websocket) | STABLE |
| [Binance Margin Testnet](https://testnet.binance.vision/) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_margin_websocket(stream_data_json)`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_margin_websocket) | STABLE |
| [Binance Isolated Margin](https://www.binance.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_isolated_margin_websocket(stream_data_json)`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_isolated_margin_websocket) | STABLE |
| [Binance Isolated Margin Testnet](https://testnet.binance.vision/) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_isolated_margin_websocket(stream_data_json)`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_isolated_margin_websocket) | STABLE |
| [Binance Futures](https://www.binance.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_futures_websocket(stream_data_json)`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_futures_websocket) | STABLE |
| [Binance Futures Testnet](https://testnet.binancefuture.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_futures_websocket(stream_data_json)`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_coin_futures_websocket) | STABLE |
| [Binance Coin Futures](https://www.binance.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_coin_futures_websocket(stream_data_json)`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_coin_futures_websocket) | NEEDS_YOUR_HELP |
| [Binance Coin Futures Testnet](https://testnet.binancefuture.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_coin_futures_websocket(stream_data_json)`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_futures_websocket) | NEEDS_YOUR_HELP |
| [Binance Jersey](https://www.binance.je) ([API](https://github.com/binance-jersey/binance-official-api-docs/)) | [`binance_je_websocket(stream_data_json)`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_je_websocket) | STABLE |
| [Binance US](https://www.binance.us) ([API](https://github.com/binance-us/binance-official-api-docs)) | [`binance_us_websocket(stream_data_json)`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_us_websocket) | STABLE |
| [Binance TR](https://www.trbinance.com) ([API](https://www.trbinance.com/apidocs)) | [`trbinance_com_websocket(stream_data_json)`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.trbinance_com_websocket) | STABLE |
| [Binance JEX](https://www.jex.com) ([API](https://jexapi.github.io/api-doc/spot.html#change-log)) | [`jex_com_websocket(stream_data_json)`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.jex_com_websocket) | STABLE |
| [Binance DEX](https://www.binance.org) ([API](https://docs.binance.org/)) | [`binance_org_websocket(stream_data_json)`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_org_websocket) | NEEDS_YOUR_HELP |
| [Binance DEX Testnet](https://testnet.binance.org) ([API](https://docs.binance.org/)) | [`binance_org_websocket(stream_data_json)`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_org_websocket) | NEEDS_YOUR_HELP |

### REST
- none

If you like the project, please 
[![star](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-fy/master/images/misc/star.png)](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/stargazers) it on 
[GitHub](https://github.com/LUCIT-Systems-and-Development/unicorn-fy)! 

## Installation and Upgrade
The module requires Python 3.6.0 or above. 

The current dependencies are listed 
[here](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/blob/master/requirements.txt).

### A wheel of the latest release with PIP from [PyPI](https://pypi.org/project/unicorn-fy/)
`pip install unicorn-fy --upgrade`

### From source of the latest release with PIP from [Github](https://github.com/LUCIT-Systems-and-Development/unicorn-fy)

#### Linux, macOS, ...
Run in bash:

`pip install https://github.com/LUCIT-Systems-and-Development/unicorn-fy/archive/$(curl -s https://api.github.com/repos/lucit-systems-and-development/unicorn-fy/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")').tar.gz --upgrade`

#### Windows
Use the below command with the version (such as 0.7.0) you determined [here](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/releases/latest):

`pip install https://github.com/LUCIT-Systems-and-Development/unicorn-fy/archive/0.7.0.tar.gz --upgrade`

### From the latest source (dev-stage) with PIP from [Github](https://github.com/LUCIT-Systems-and-Development/unicorn-fy)
This is not a release version and can not be considered to be stable!

`pip install https://github.com/LUCIT-Systems-and-Development/unicorn-fy/tarball/master --upgrade`

### [Conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), [Virtualenv](https://virtualenv.pypa.io/en/latest/) or plain [Python](https://docs.python.org/2/install/)
Download the [latest release](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/releases/latest) 
or the [current master branch](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/archive/master.zip)
 and use:
 
- ./environment.yml
- ./requirements.txt
- ./setup.py

## Change Log
[https://unicorn-fy.docs.lucit.tech//CHANGELOG.html](https://unicorn-fy.docs.lucit.tech//CHANGELOG.html)

## Documentation
- [General](https://unicorn-fy.docs.lucit.tech/)
- [Modules](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html)

## Examples
- [example_logging.py](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/blob/master/example_logging.py)
- [example_unicorn_fy.py](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/blob/master/example_unicorn_fy.py)
- [example_version_of_this_package.py](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/blob/master/example_version_of_this_package.py)

## Project Homepage
[https://github.com/LUCIT-Systems-and-Development/unicorn-fy](https://github.com/LUCIT-Systems-and-Development/unicorn-fy)

## Wiki
[https://github.com/LUCIT-Systems-and-Development/unicorn-fy/wiki](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/wiki)

## Social
- [Discussions](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/discussions)
- [https://t.me/unicorndevs](https://t.me/unicorndevs)
- [https://dev.binance.vision](https://dev.binance.vision)
- [https://community.binance.org](https://community.binance.org)

## Receive Notifications
To receive notifications on available updates you can 
[![watch](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-fy/master/images/misc/watch.png)](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/watchers) 
the repository on [GitHub](https://github.com/LUCIT-Systems-and-Development/unicorn-fy), write your 
[own script](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/blob/master/example_version_of_this_package.py) 
with using 
[`is_update_available()`](https://unicorn-fy.docs.lucit.tech//unicorn_fy.html?highlight=is_update#unicorn_fy.unicorn_fy.UnicornFy.is_update_availabe) 
 or you use the 
[monitoring API service](https://github.com/LUCIT-Systems-and-Development/unicorn-binance-websocket-api/wiki/UNICORN-Monitoring-API-Service).

Follow us on [Twitter](https://twitter.com/LUCIT_SysDev) or on [Facebook](https://www.facebook.com/lucit.systems.and.development) for general news about the [unicorn-binance-suite](https://www.lucit.tech/unicorn-binance-suite.html)!

## How to report Bugs or suggest Improvements?
[List of planned features](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement) - 
click ![thumbs-up](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-fy/master/images/misc/thumbup.png) if you need one of them or suggest a new feature!

Before you report a bug, [try the latest release](https://github.com/LUCIT-Systems-and-Development/unicorn-fy#installation-and-upgrade). 
If the issue still exists, provide the error trace, OS and python version and explain how to reproduce the error. 
A demo script is appreciated.

If you dont find an issue related to your topic, please open a new issue:
[https://github.com/LUCIT-Systems-and-Development/unicorn-fy/issues](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/issues)

[Report a security bug!](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/security/policy)

## Contributing
[UnicornFy](https://www.lucit.tech/unicorn-fy.html)  is an open 
source project which welcomes contributions which can be anything from simple documentation fixes and reporting dead links to new features. To 
contribute follow 
[this guide](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/blob/master/CONTRIBUTING.md).
 
### Contributors
[![Contributors](https://contributors-img.web.app/image?repo=lucit-systems-and-development/unicorn-fy)](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/graphs/contributors)

We ![love](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-fy/master/images/misc/heart.png) open source!

## Commercial Support
[![LUCIT](https://www.lucit.tech/files/images/logos/LUCIT-LOGO.png)](https://www.lucit.tech)

***Do you need a developer, operator or consultant?***

Contact [me](https://about.me/oliver-zehentleitner) for a non-binding initial consultation via my company 
[LUCIT](https://www.lucit.tech) from Vienna (Austria) or via [Telegram](https://t.me/LUCIT_OZ).
