#!/usr/bin/env bash

rm *.py.log
rm dev/*.log

rm build -r
rm dist -r
rm *.egg-info -r
rm stubs -r
rm out -r

rm unicorn_fy/*.c
rm unicorn_fy/*.html
rm unicorn_fy/*.dll
rm unicorn_fy/*.so
rm unicorn_fy/*.pyi