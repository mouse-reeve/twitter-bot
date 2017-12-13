#!/bin/bash

source venv/bin/activate
python3 setup.py install
python3 tests/tests.py
