[![Get a UNICORN Binance Suite License](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/unicorn-binance-suite/master/images/logo/LUCIT-UBS-License-Offer.png)](https://shop.lucit.services)

[![GitHub Release](https://img.shields.io/github/release/LUCIT-Systems-and-Development/unicorn-fy.svg?label=github)](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/releases)
[![GitHub Downloads](https://img.shields.io/github/downloads/LUCIT-Systems-and-Development/unicorn-fy/total?color=blue)](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/releases)
![Anaconda Release](https://img.shields.io/conda/v/lucit/unicorn-fy?color=blue)
![Anaconda Downloads](https://img.shields.io/conda/dn/lucit/unicorn-fy?color=blue)
[![PyPi Release](https://img.shields.io/pypi/v/unicorn-fy?color=blue)](https://pypi.org/project/unicorn-fy/)
[![PyPi Downloads](https://pepy.tech/badge/unicorn-fy)](https://pepy.tech/project/unicorn-fy)
[![License](https://img.shields.io/github/license/LUCIT-Systems-and-Development/unicorn-fy.svg?color=blue)](https://unicorn-fy.docs.lucit.tech/license.html)
[![Supported Python Version](https://img.shields.io/pypi/pyversions/unicorn_fy.svg)](https://www.python.org/downloads/)
[![PyPI - Status](https://img.shields.io/pypi/status/unicorn_fy.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/issues)
[![codecov](https://codecov.io/gh/LUCIT-Systems-and-Development/unicorn-fy/branch/master/graph/badge.svg?token=5I03AZ3F5S)](https://codecov.io/gh/LUCIT-Systems-and-Development/unicorn-fy)
[![CodeQL](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/actions/workflows/codeql-analysis.yml)
[![Unit Tests](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/actions/workflows/unit-tests.yml)
[![Build and Publish GH+PyPi](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/actions/workflows/build_wheels.yml/badge.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/actions/workflows/build_wheels.yml)
[![Build and Publish Anaconda](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/actions/workflows/build_conda.yml/badge.svg)](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/actions/workflows/build_conda.yml)
[![Read the Docs](https://img.shields.io/badge/read-%20docs-yellow)](https://unicorn-fy.docs.lucit.tech/)
[![Read How To`s](https://img.shields.io/badge/read-%20howto-yellow)](https://medium.lucit.tech)
[![Github](https://img.shields.io/badge/source-github-cbc2c8)](https://github.com/LUCIT-Systems-and-Development/unicorn-fy)
[![Telegram](https://img.shields.io/badge/community-telegram-41ab8c)](https://t.me/unicorndevs)
[![Gitter](https://img.shields.io/badge/community-gitter-41ab8c)](https://gitter.im/unicorn-binance-suite/unicorn-fy?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Get Free Professional Support](https://img.shields.io/badge/chat-lucit%20support-004166)](https://www.lucit.tech/get-support.html)
[![ChatGPT UNICORN Binance Suite Assistant](https://img.shields.io/badge/chatgpt-%20ubs%20assistant-DA70D6)](https://chat.openai.com/g/g-VjCOjRhCJ-unicorn-binance-suite-assistant)

[![LUCIT-UNICORNFY-Banner](https://raw.githubusercontent.com/lucit-systems-and-development/unicorn-fy/master/images/logo/LUCIT-UNICORNFY-Banner-Readme.png)](https://www.lucit.tech/unicorn-fy.html)

# UnicornFy
[Supported Exchanges](#supported-exchanges) | [Installation](#installation-and-upgrade) | [Change Log](#change-log) | [Documentation](#documentation) | 
[Examples](#examples) | [Wiki](#wiki) | [Social](#social) | [Notifications](#receive-notifications) | [Bugs](#how-to-report-bugs-or-suggest-improvements) 
| [Contributing](#contributing) | [Disclaimer](#disclaimer) | [Commercial Support](#commercial-support)

A Python API by [LUCIT](https://www.lucit.tech) to convert received raw data from crypto exchange API endpoints 
into well-formed python dictionaries.

Part of ['UNICORN Binance Suite'](https://www.lucit.tech/unicorn-binance-suite.html).

Get help with the integration of the `UNICORN Binance Suite` modules from the 
[`UNICORN Binance Suite Assistant` GPT](https://chat.openai.com/g/g-VjCOjRhCJ-unicorn-binance-suite-assistant) or 
[a real human LUCIT employee](https://www.lucit.tech/get-support.html).

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

ufy = unicorn_fy.UnicornFy()

unicorn_fied_stream_data = ufy.binance_com_websocket(received_stream_data_json)
print(unicorn_fied_stream_data)
```

Output:

```
{'stream_type': 'btcusdt@trade', 'event_type': 'trade', 'event_time': 1556876873656, 'symbol': 'BTCUSDT',
 'trade_id': 117727701, 'price': '5786.76000000', 'quantity': '0.03200500', 'buyer_order_id': 341831847,
 'seller_order_id': 341831876, 'trade_time': 1556876873648, 'is_market_maker': True, 'ignore': True,
 'unicorn_fied': ['binance', '0.13.1']}
```

This lib is integrated into 
[UNICORN Binance WebSocket API](https://www.lucit.tech/unicorn-binance-websocket-api.html) 
and can be activated by setting parameter 
[`output_default` of `BinanceWebSocketApiManager()` to `UnicornFy`](https://lucit-systems-and-development.github.io/unicorn-binance-websocket-api/unicorn_binance_websocket_api.html?highlight=output_default#module-unicorn_binance_websocket_api.manager) 
or for specific streams with the parameter 
[`output` of `create_stream()` to `UnicornFy`](https://lucit-systems-and-development.github.io/unicorn-binance-websocket-api/unicorn_binance_websocket_api.html?highlight=output#unicorn_binance_websocket_api.manager.BinanceWebSocketApiManager.create_stream).

## Get the right [logger](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/blob/master/example_logging.py):
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
The module requires Python 3.7.0 or above. 

For the PyPy interpreter we offer packages only from Python version 3.9 and higher.

The current dependencies are listed 
[here](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/blob/master/requirements.txt).

If you run into errors during the installation take a look [here](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/wiki/Installation).

### A Cython binary, PyPy or source code based CPython wheel of the latest version with `pip` from [PyPI](https://pypi.org/project/unicorn-binance-rest-api/)
Our [Cython](https://cython.org/) and [PyPy](https://www.pypy.org/) Wheels are available on [PyPI](https://pypi.org/), 
these wheels offer significant advantages for Python developers:

- ***Performance Boost with Cython Wheels:*** Cython is a programming language that supplements Python with static typing and C-level performance. By compiling 
  Python code into C, Cython Wheels can significantly enhance the execution speed of Python code, especially in 
  computationally intensive tasks. This means faster runtimes and more efficient processing for users of our package. 

- ***PyPy Wheels for Enhanced Efficiency:*** PyPy is an alternative Python interpreter known for its speed and efficiency. It uses Just-In-Time (JIT) compilation, 
  which can dramatically improve the performance of Python code. Our PyPy Wheels are tailored for compatibility with 
  PyPy, allowing users to leverage this speed advantage seamlessly.

Both Cython and PyPy Wheels on PyPI make the installation process simpler and more straightforward. They ensure that 
you get the optimized version of our package with minimal setup, allowing you to focus on development rather than 
configuration.

#### Installation
`pip install unicorn-fy`

#### Update
`pip install unicorn-fy --upgrade`

### A Conda Package of the latest version with `conda` from [Anaconda](https://anaconda.org/lucit)
The `unicorn-fy` package is also available as a Cython version for the `linux-64`, `osx-64` 
and `win-64` architectures with [Conda](https://docs.conda.io/en/latest/) through the 
[`lucit` channel](https://anaconda.org/lucit). 

For optimal compatibility and performance, it is recommended to source the necessary dependencies from the 
[`conda-forge` channel](https://anaconda.org/conda-forge). 

#### Installation
```
conda config --add channels conda-forge
conda config --add channels lucit
conda install -c lucit unicorn-fy
```

#### Update
`conda update -c lucit unicorn-fy`

### From source of the latest release with PIP from [Github](https://github.com/LUCIT-Systems-and-Development/unicorn-fy)

#### Linux, macOS, ...
Run in bash:

`pip install https://github.com/LUCIT-Systems-and-Development/unicorn-fy/archive/$(curl -s https://api.github.com/repos/lucit-systems-and-development/unicorn-fy/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")').tar.gz --upgrade`

#### Windows
Use the below command with the version (such as 0.13.1) you determined [here](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/releases/latest):

`pip install https://github.com/LUCIT-Systems-and-Development/unicorn-fy/archive/0.13.1.tar.gz --upgrade`

### From the latest source (dev-stage) with PIP from [GitHub](https://github.com/LUCIT-Systems-and-Development/unicorn-fy)
This is not a release version and can not be considered to be stable!

`pip install https://github.com/LUCIT-Systems-and-Development/unicorn-fy/tarball/master --upgrade`

### [Conda environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html), [Virtualenv](https://virtualenv.pypa.io/en/latest/) or plain [Python](https://www.python.org)
Download the [latest release](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/releases/latest) 
or the [current master branch](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/archive/master.zip)
 and use:
 
- ./environment.yml
- ./meta.yaml
- ./pyproject.toml
- ./requirements.txt
- ./setup.py

## Change Log
[https://unicorn-fy.docs.lucit.tech//CHANGELOG.html](https://unicorn-fy.docs.lucit.tech//CHANGELOG.html)

## Documentation
- [General](https://unicorn-fy.docs.lucit.tech/)
- [Modules](https://unicorn-fy.docs.lucit.tech/modules.html)

## Examples
- [example_logging.py](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/blob/master/example_logging.py)
- [example_unicorn_fy.py](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/blob/master/example_unicorn_fy.py)
- [example_version_of_this_package.py](https://github.com/LUCIT-Systems-and-Development/unicorn-fy/blob/master/example_version_of_this_package.py)

## Project Homepage
[https://www.lucit.tech/unicorn-fy.html](https://www.lucit.tech/unicorn-fy.html)

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

Follow us on [GitHub](https://github.com/LUCIT-Systems-and-Development), [Medium](https://medium.lucit.tech/),
[YouTube](https://www.youtube.com/@LUCIT_Systems_and_Development), 
[LinkedIn](https://www.linkedin.com/company/lucit-systems-and-development), 
[X](https://twitter.com/LUCIT_SysDev) or [Facebook](https://www.facebook.com/lucit.systems.and.development)!

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

## Disclaimer
This project is for informational purposes only. You should not construe this information or any other material as 
legal, tax, investment, financial or other advice. Nothing contained herein constitutes a solicitation, recommendation, 
endorsement or offer by us or any third party provider to buy or sell any securities or other financial instruments in 
this or any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such 
jurisdiction.

### If you intend to use real money, use it at your own risk!

Under no circumstances will we be responsible or liable for any claims, damages, losses, expenses, costs or liabilities 
of any kind, including but not limited to direct or indirect damages for loss of profits.

## Commercial Support

[![Get professional and fast support](https://raw.githubusercontent.com/LUCIT-Systems-and-Development/unicorn-binance-suite/master/images/support/LUCIT-get-professional-and-fast-support.png)](https://www.lucit.tech/get-support.html)

***Do you need a developer, operator or consultant?*** [Contact us](https://www.lucit.tech/contact.html) for a non-binding initial consultation!
