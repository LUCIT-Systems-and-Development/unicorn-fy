#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# File: pypi_create_wheel.sh
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

security-check() {
    echo -n "Did you change the version in \`sphinx conf.py\` and \`unicorn_fy.py\`? [yes|NO] "
    local SURE
    read SURE
    if [ "$SURE" != "yes" ]; then
        exit 1
    fi
    echo "ok, lets go ..."
}

security-check
python3 setup.py bdist_wheel
