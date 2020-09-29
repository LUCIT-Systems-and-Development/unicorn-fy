# unicorn_fy Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).

## 0.6.0.dev (development stage/unreleased/unstable)

## 0.6.0
### Added
- Binance-com-margin
- Binance-com-isolated_margin
- Jex.com

## 0.5.0
### Added
- `outboundAccountPosition` [issue#11](https://github.com/oliver-zehentleitner/unicorn_fy/issues/11) - thanks to 
@bmschwartz
- handling for results
### Fixed
- `ModuleNotFoundError: No module named 'unicorn_fy.unicorn_fy'; 'unicorn_fy' is not a package` 
[PR#10](https://github.com/oliver-zehentleitner/unicorn_fy/pull/10), [issue#9](https://github.com/oliver-zehentleitner/unicorn_fy/issues/9)
- thanks to @uggel

## 0.4.1
### Added
- `account_permissions` in `outboundAccountInfo`

## 0.4.0
### Fixed
- all kind of tickers
- result msg handling
- error msg handling
### Removed
- Exception handling to show python error trace

## 0.3.5
### Fixed
- `!miniTicker@arr` structure

## 0.3.4
### Fixed
- `!miniTicker@arr` structure

## 0.3.3
### Added
- TypeError exception

## 0.3.2
### Changed
- ujson instead of stock json
- exception handling
### Added
- binance.com-futures (copy of binance_websocket() with suggested modification of 
[issue #1](https://github.com/oliver-zehentleitner/unicorn_fy/issues/1))

## 0.3.1
### Changes
- Moved docs to github pages

## 0.3.0
### Adding
- binance_us_websocket()
### Changes
- exchange name to return dict

## 0.2.0
### Adding
- binance_com_websocket()
- binance_je_websocket()
- is_update_availabe()
- get_latest_version()
- get_version()
- get_latest_release_info()

### Depricated
- binance_websocket()

## 0.1.1
### Fixed
- create pypi package

## 0.1.0 
- Released
