#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File: setup.py
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

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='unicorn_fy',
     version='0.5.0a',
     author="Oliver Zehentleitner",
     url="https://github.com/oliver-zehentleitner/unicorn_fy",
     description="Convert received raw data from crypto exchange API endpoints into well-formed python dictionaries.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='MIT License',
     install_requires=['ujson'],
     keywords='binance, api, exchange, unify, binance-dex, binance-chain, rest-api, websockets',
     project_urls={
        'Documentation': 'https://oliver-zehentleitner.github.io/unicorn_fy/',
        'Wiki': 'https://github.com/oliver-zehentleitner/unicorn_fy/wiki',
        'Author': 'https://about.me/oliver-zehentleitner/',
     },
     packages=setuptools.find_packages(),
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
         "License :: OSI Approved :: MIT License",
         'Intended Audience :: Developers',
         "Intended Audience :: Financial and Insurance Industry",
         "Intended Audience :: Information Technology",
         "Intended Audience :: Science/Research",
         "Operating System :: OS Independent",
         "Topic :: Office/Business :: Financial :: Investment",
         'Topic :: Software Development :: Libraries :: Python Modules',
     ],
)
