#!/bin/sh

pip install pipenv
pipenv lock -r > requirements.txt
pip install -r requirements.txt -t dist
zip -r lambda_layer.zip dist
