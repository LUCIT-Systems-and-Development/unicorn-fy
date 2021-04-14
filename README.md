[![GitHub release](https://img.shields.io/github/release/oliver-zehentleitner/unicorn-fy.svg)](https://github.com/oliver-zehentleitner/unicorn-fy/releases/latest)
[![GitHub](https://img.shields.io/github/license/oliver-zehentleitner/unicorn-fy.svg?color=blue)](https://github.com/oliver-zehentleitner/unicorn-fy/blob/master/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/unicorn_fy.svg)](https://www.python.org/downloads/)
[![Downloads](https://pepy.tech/badge/unicorn-fy)](https://pepy.tech/project/unicorn-fy)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/unicorn_fy.svg?label=PyPI%20wheel)](https://pypi.org/project/unicorn-fy/)
[![PyPI - Status](https://img.shields.io/pypi/status/unicorn_fy.svg)](https://github.com/oliver-zehentleitner/unicorn-fy/issues)
[![build](https://github.com/oliver-zehentleitner/unicorn-fy/actions/workflows/python-app.yml/badge.svg)](https://github.com/oliver-zehentleitner/unicorn-fy/actions/workflows/python-app.yml)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/oliver-zehentleitner/unicorn-fy.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/oliver-zehentleitner/unicorn-fy/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/oliver-zehentleitner/unicorn-fy.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/oliver-zehentleitner/unicorn-fy/context:python)
[![codecov](https://codecov.io/gh/oliver-zehentleitner/unicorn-fy/branch/master/graph/badge.svg?token=5I03AZ3F5S)](https://codecov.io/gh/oliver-zehentleitner/unicorn-fy)
[![Telegram](https://img.shields.io/badge/chat-telegram-yellow.svg)](https://t.me/unicorndevs)
[![Donations/week](http://img.shields.io/liberapay/receives/oliver-zehentleitner.svg?logo=liberapay)](https://liberapay.com/oliver-zehentleitner/donate)
[![Patrons](http://img.shields.io/liberapay/patrons/oliver-zehentleitner.svg?logo=liberapay")](https://liberapay.com/oliver-zehentleitner/donate)

# UnicornFy
[Supported Exchanges](#supported-exchanges) | [Installation](#installation-and-upgrade) | [Documentation](#documentation) | 
[Change Log](#change-log) | [Wiki](#wiki) | [Social](#social) | [Notifications](#receive-notifications) | 
[Bugs](#how-to-report-bugs-or-suggest-improvements) | [Contributing](#contributing) | [Commercial Support](#commercial-support) | [Donate](#donate)

Convert received raw data from crypto exchange API endpoints into well-formed python dictionaries.

Part of ['UNICORN Binance Suite'](https://github.com/oliver-zehentleitner/unicorn-binance-suite).

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

unicorn_fied_stream_data = UnicornFy.binance_com_websocket(received_stream_data_json)
print(unicorn_fied_stream_data)
>>>
{'stream_type': 'btcusdt@trade', 'event_type': 'trade', 'event_time': 1556876873656, 'symbol': 'BTCUSDT', 'trade_id': 117727701, 'price': '5786.76000000', 'quantity': '0.03200500', 'buyer_order_id': 341831847, 'seller_order_id': 341831876, 'trade_time': 1556876873648, 'is_market_maker': True, 'ignore': True, 'unicorn_fied': ['binance', '0.1.0']}
```

## Supported Exchanges
### Websockets

| Exchange | Docs            | Status | 
| -------- | --------------- | ------ |
| [Binance](https://www.binance.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_websocket) | STABLE |
| [Binance Testnet](https://testnet.binance.vision/) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_websocket) | STABLE |
| [Binance Margin](https://www.binance.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_margin_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_margin_websocket) | STABLE |
| [Binance Margin Testnet](https://testnet.binance.vision/) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_margin_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_margin_websocket) | STABLE |
| [Binance Isolated Margin](https://www.binance.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_isolated_margin_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_isolated_margin_websocket) | STABLE |
| [Binance Isolated Margin Testnet](https://testnet.binance.vision/) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_isolated_margin_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_isolated_margin_websocket) | STABLE |
| [Binance Futures](https://www.binance.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_futures_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_futures_websocket) | STABLE |
| [Binance Futures Testnet](https://testnet.binancefuture.com) ([API](https://github.com/binance-exchange/binance-official-api-docs)) | [`binance_com_futures_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_com_futures_websocket) | STABLE |
| [Binance Jersey](https://www.binance.je) ([API](https://github.com/binance-jersey/binance-official-api-docs/)) | [`binance_je_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_je_websocket) | STABLE |
| [Binance US](https://www.binance.us) ([API](https://github.com/binance-us/binance-official-api-docs)) | [`binance_us_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_us_websocket) | STABLE |
| [Binance TR](https://www.trbinance.com) ([API](https://www.trbinance.com/apidocs)) | [`trbinance_com_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.trbinance_com_websocket) | STABLE |
| [Binance JEX](https://www.jex.com) ([API](https://jexapi.github.io/api-doc/spot.html#change-log)) | [`jex_com_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.jex_com_websocket) | STABLE |
| [Binance DEX](https://www.binance.org) ([API](https://docs.binance.org/)) | [`binance_org_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_org_websocket) | NEEDS_YOUR_HELP |
| [Binance DEX Testnet](https://testnet.binance.org) ([API](https://docs.binance.org/)) | [`binance_org_websocket(stream_data_json)`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=binance_com#unicorn_fy.unicorn_fy.UnicornFy.binance_org_websocket) | NEEDS_YOUR_HELP |

### REST
- none

If you like the project, please 
[![star](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-fy/master/images/misc/star.png)](https://github.com/oliver-zehentleitner/unicorn-fy/stargazers) it on 
[GitHub](https://github.com/oliver-zehentleitner/unicorn-fy)! 

## Installation and Upgrade
The module requires Python 3.6.0 or above. 

The current dependencies are listed 
[here](https://github.com/oliver-zehentleitner/unicorn-fy/blob/master/requirements.txt).

### A wheel of the latest release with PIP from [PyPI](https://pypi.org/project/unicorn-fy/)
`pip install unicorn-fy --upgrade`

### From source of the latest release with PIP from [Github](https://github.com/oliver-zehentleitner/unicorn-fy)

#### Linux, macOS, ...
Run in bash:

`pip install https://github.com/oliver-zehentleitner/unicorn-fy/archive/$(curl -s https://api.github.com/repos/oliver-zehentleitner/unicorn-fy/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")').tar.gz --upgrade`

#### Windows
Use the below command with the version (such as 0.7.0) you determined [here](https://github.com/oliver-zehentleitner/unicorn-fy/releases/latest):

`pip install https://github.com/oliver-zehentleitner/unicorn-fy/archive/0.7.0.tar.gz --upgrade`

### From the latest source (dev-stage) with PIP from [Github](https://github.com/oliver-zehentleitner/unicorn-fy)
This is not a release version and can not be considered to be stable!

`pip install https://github.com/oliver-zehentleitner/unicorn-fy/tarball/master --upgrade`

### [Conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), [Virtualenv](https://virtualenv.pypa.io/en/latest/) or plain [Python](https://docs.python.org/2/install/)
Download the [latest release](https://github.com/oliver-zehentleitner/unicorn-fy/releases/latest) 
or the [current master branch](https://github.com/oliver-zehentleitner/unicorn-fy/archive/master.zip)
 and use:
- ./environment.yml
- ./requirements.txt
- ./setup.py

## Documentation
- [General](https://oliver-zehentleitner.github.io/unicorn-fy)
- [Modules](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html)

## Source, Downloads, Examples, ...
[https://github.com/oliver-zehentleitner/unicorn-fy](https://github.com/oliver-zehentleitner/unicorn-fy)

## Change Log
[https://oliver-zehentleitner.github.io/unicorn-fy/CHANGELOG.html](https://oliver-zehentleitner.github.io/unicorn-fy/CHANGELOG.html)

## Wiki
[https://github.com/oliver-zehentleitner/unicorn-fy/wiki](https://github.com/oliver-zehentleitner/unicorn-fy/wiki)

## Social
- [https://t.me/unicorndevs](https://t.me/unicorndevs)
- [Twitter](https://twitter.com/DevsUnicorn)
- [unicorn-coding-club](https://github.com/oliver-zehentleitner/unicorn-coding-club)
- [https://dev.binance.vision](https://dev.binance.vision)
- [https://community.binance.org](https://community.binance.org)

## Receive Notifications
To receive notifications on available updates you can 
[![watch](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-fy/master/images/misc/watch.png)](https://github.com/oliver-zehentleitner/unicorn-fy/watchers) 
the repository on [GitHub](https://github.com/oliver-zehentleitner/unicorn-fy), write your 
[own script](https://github.com/oliver-zehentleitner/unicorn-fy/blob/master/example_version_of_this_package.py) 
with using 
[`is_update_availabe()`](https://oliver-zehentleitner.github.io/unicorn-fy/unicorn_fy.html?highlight=is_update#unicorn_fy.unicorn_fy.UnicornFy.is_update_availabe) 
 or you use the 
[monitoring API service](https://github.com/oliver-zehentleitner/unicorn-binance-websocket-api/wiki/UNICORN-Monitoring-API-Service).

## How to report Bugs or suggest Improvements?
[List of planned features](https://github.com/oliver-zehentleitner/unicorn-fy/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement) - 
click ![thumbs-up](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-fy/master/images/misc/thumbup.png) if you need one of them or suggest a new feature!

Before you report a bug, [try the latest release](https://github.com/oliver-zehentleitner/unicorn-fy#installation-and-upgrade). 
If the issue still exists, provide the error trace, OS and python version and explain how to reproduce the error. 
A demo script is appreciated.

If you dont find an issue related to your topic, please open a new issue:
[https://github.com/oliver-zehentleitner/unicorn-fy/issues](https://github.com/oliver-zehentleitner/unicorn-fy/issues)

[Report a security bug!](https://github.com/oliver-zehentleitner/unicorn-fy/security/policy)

## Contributing
[unicorn-fy](https://github.com/oliver-zehentleitner/unicorn-fy)  is an open 
source project which welcomes contributions which can be anything from simple documentation fixes and reporting dead links to new features. To 
contribute follow 
[this guide](https://github.com/oliver-zehentleitner/unicorn-fy/blob/master/CONTRIBUTING.md).
 
### Contributors
[![Contributors](https://contributors-img.web.app/image?repo=oliver-zehentleitner/unicorn-fy)](https://github.com/oliver-zehentleitner/unicorn-fy/graphs/contributors)

We ![love](https://raw.githubusercontent.com/oliver-zehentleitner/unicorn-fy/master/images/misc/heart.png) open source!

## Commercial Support
Need a Python developer or consulting? 

Contact [me](https://about.me/oliver-zehentleitner) for a non-binding and free consultation via my company 
[LUCIT](https://www.lucit.dev) from Vienna (Austria) or via [Telegram](https://t.me/LUCIT_OZ).

## Donate
Developing, documenting and testing the 
[UNICORN Binance Suite](https://github.com/oliver-zehentleitner/unicorn-binance-suite) and supporting the community 
takes a lot of time and time is a form of cost. I am extremely happy to do this, but need a solution for sharing the 
costs.

I think we are lucky, as our community consists of traders and programmers I expect to find mostly rational thinking 
people who also benefit financially from these libraries.

I would like to create a fair model for funding. My goals are that unicorn-binance-websocket-api, 
unicorn-binance-rest-api and unicorn-fy remain freely available as open source and that I am compensated at least to 
some extent and thus can invest my time more easily.

If you know the hooker principle from negotiation research or game theory, you know about the problem that people don't 
often pay for something out of their own impulse if they have already received it for free. 

So my idea is to give every donor who gives an amount over 50 EUR access to a private Github repository where Python 
classes for trading algos are provided (OrderBook, advanced stop-loss, ...). Moreover, maybe a nice ApiTrader community 
will be formed.

So the donor not only helps to push the open source development but also gets access to a well maintained collection of 
practical code for little money. 

Furthermore community members can help me by donating own developments to make the 
[unicorn-coding-club](https://github.com/oliver-zehentleitner/unicorn-coding-club) repository more attractive to create 
further incentives for new donors. This way we generate added value for all sides in an uncomplicated way.

If you donated at least 50 EUR (without transaction fee), please send me a message with a confirmation and your Github 
username via https://www.lucit-development.co/contact.html, I will invite you to the 
[unicorn-coding-club](https://github.com/oliver-zehentleitner/unicorn-coding-club) as soon as possible.

[![Donate using Liberapay](https://liberapay.com/assets/widgets/donate.svg)](https://liberapay.com/oliver-zehentleitner/donate)
[Donate with GitHub](https://github.com/sponsors/oliver-zehentleitner/)
```
Terra (LUNA, UST, ...): terra1yt34qmmycextztnj9mpt3mnjzqqvl8jtqqq7g9
BTC: 39fS74fvcGnmEk8JUV8bG6P1wkdH29GtsA
DASH: XsRhBuPkXGF9WvifdpkVhTGSmVT4VcuQZ7
ETH: 0x1C15857Bf1E18D122dDd1E536705748aa529fc9C
LTC: LYNzHMFUbee3siyHvNCPaCjqXxjyq8YRGJ
XMR: 85dzsTRh6GRPGVSJoUbFDwAf9uwwAdim1HFpiGshLeKHgj2hVqKtYVPXMZvudioLsuLS1AegkUiQ12jwReRwWcFvF7kDAbF
ZEC: t1WvQMPJMriGWD9qkZGDdE9tTJaawvmsBie
```
