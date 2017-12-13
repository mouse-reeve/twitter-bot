#!/bin/bash

source venv/bin/activate
python setup.py install
python tests/tests.py
