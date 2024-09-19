#!/usr/bin/env bash

rem Note, i could not make this work without this command locally:
rem git update-index --chmod=+x tests/test.sh

python src/software_title/script.py --a "A string" --b 5.7
