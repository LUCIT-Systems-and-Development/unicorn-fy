#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File: setup.py
#
# Part of ‘UnicornFy’
# Project website: https://github.com/unicorn-data-analysis/unicorn_fy
# Documentation: https://www.unicorn-data.com/unicorn_fy.html
# PyPI: https://pypi.org/project/unicorn-fy/
#
# Author: UNICORN Data Analysis
#         https://www.unicorn-data.com/
#
# Copyright (c) 2019, UNICORN Data Analysis
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
     version='0.1.1',
     author="UNICORN Data Analysis",
     url="https://www.unicorn-data.com",
     scripts=['unicorn_fy.py'],
     description="Convert received raw data from crypto exchange API endpoints into well-formed python dictionaries.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='MIT License',
     install_requires=[],
     keywords='unicorn-data-analysis, binance, api, exchange, unify, binance-dex, binance-chain, rest-api, websockets',
     project_urls={
        'Documentation': 'https://www.unicorn-data.com/unicorn_fy',
        'Wiki': 'https://github.com/unicorn-data-analysis/unicorn_fy/wiki',
        'Source': 'https://github.com/unicorn-data-analysis/unicorn_fy',
     },
     packages=setuptools.find_packages(),
     classifiers=[
         "Development Status :: 4 - Beta",
         "Programming Language :: Python :: 2",
         "Programming Language :: Python :: 3",
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
