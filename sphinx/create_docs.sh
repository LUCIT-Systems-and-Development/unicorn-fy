#!/usr/bin/env bash

rm source/changelog.md
rm source/code_of_conduct.md
rm source/contributing.md
rm source/license.rst
rm source/readme.md
rm source/security.md

cp ../CHANGELOG.md source/changelog.md
cp ../CODE_OF_CONDUCT.md source/code_of_conduct.md
cp ../CONTRIBUTING.md source/contributing.md
cp ../LICENSE source/license.rst
cp ../README.md source/readme.md
cp ../SECURITY.md source/security.md

make html -d
