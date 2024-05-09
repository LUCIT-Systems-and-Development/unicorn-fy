#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# File: setup.py
#
# Part of ‘UnicornFy’
# Project website: https://www.lucit.tech/unicorn-fy.html
# Github: https://github.com/LUCIT-Systems-and-Development/unicorn-fy
# Documentation: https://unicorn-fy.docs.lucit.tech/
# PyPI: https://pypi.org/project/unicorn-fy
# LUCIT Online Shop: https://shop.lucit.services/software
#
# License: LSOSL - LUCIT Synergetic Open Source License
# https://github.com/LUCIT-Systems-and-Development/unicorn-fy/blob/master/LICENSE
#
# Author: LUCIT Systems and Development
#
# Copyright (c) 2019-2023, LUCIT Systems and Development (https://www.lucit.tech)
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

from Cython.Build import cythonize
from setuptools import setup, find_packages, Extension
import os
import shutil
import subprocess

name = "unicorn-fy"
source_dir = "unicorn_fy"

stubs_dir = "stubs"
extensions = [
    Extension("*", [f"{source_dir}/*.py"]),
]

# Setup
print("Generating stub files ...")
os.makedirs(stubs_dir, exist_ok=True)
for filename in os.listdir(source_dir):
    if filename.endswith('.py'):
        source_path = os.path.join(source_dir, filename)
        subprocess.run(['stubgen', '-o', stubs_dir, source_path], check=True)
for stub_file in os.listdir(os.path.join(stubs_dir, source_dir)):
    if stub_file.endswith('.pyi'):
        source_stub_path = os.path.join(stubs_dir, source_dir, stub_file)
        if os.path.exists(os.path.join(source_dir, stub_file)):
            print(f"Skipped moving {source_stub_path} because {os.path.join(source_dir, stub_file)} already exists!")
        else:
            shutil.move(source_stub_path, source_dir)
            print(f"Moved {source_stub_path} to {source_dir}!")
shutil.rmtree(os.path.join(stubs_dir))
print("Stub files generated and moved successfully.")

with open("README.md", "r") as fh:
    print("Using README.md content as `long_description` ...")
    long_description = fh.read()

setup(
     name=name,
     version="0.14.2",
     author="LUCIT Systems and Development",
     author_email='info@lucit.tech',
     url="https://github.com/LUCIT-Systems-and-Development/unicorn-fy",
     description="A Python SDK by LUCIT to convert received raw data from crypto exchange API endpoints into "
                 "well-formed python dictionaries.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='LSOSL - LUCIT Synergetic Open Source License',
     install_requires=['ujson', 'requests', 'Cython'],
     keywords='binance, api, exchange, unicornfy, binance-dex, binance-chain, rest-api, websockets',
     project_urls={
         'Documentation': 'https://unicorn-fy.docs.lucit.tech',
         'Wiki': 'https://github.com/LUCIT-Systems-and-Development/unicorn-fy/wiki',
         'Author': 'https://www.lucit.tech',
         'Changes': 'https://unicorn-fy.docs.lucit.tech/changelog.html',
         'License': 'https://unicorn-fy.docs.lucit.tech/license.html',
         'Issue Tracker': 'https://github.com/LUCIT-Systems-and-Development/unicorn-fy/issues',
         'Chat': 'https://gitter.im/unicorn-binance-suite/unicorn-fy',
         'Telegram': 'https://t.me/unicorndevs', 
         'Get Support': 'https://www.lucit.tech/get-support.html',
     },
     packages=find_packages(exclude=[f"dev/{source_dir}"], include=[source_dir]),
     ext_modules=cythonize(extensions, compiler_directives={'language_level': "3"}),
     python_requires='>=3.7.0',
     package_data={'': ['*.so', '*.dll', '*.py', '*.pyd', '*.pyi']},
     include_package_data=True,
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
         "Programming Language :: Python :: 3.10",
         "Programming Language :: Python :: 3.11",
         "Programming Language :: Python :: 3.12",
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
