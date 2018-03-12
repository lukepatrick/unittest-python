#!/usr/bin/env bash

# Setup python venv

virtualenv env --no-site-packages --python=python3
source env/bin/activate
pip3 install -r requirements.txt