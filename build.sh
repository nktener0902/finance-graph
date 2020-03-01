#!/bin/bash  

rm -rf dist  
mkdir dist  
#cp -r src/* dist  
pipenv lock -r > requirements.txt  
pip install -r requirements.txt -t dist  
zip -r lambda_function.zip ./dist/*  
#rm requirements.txt  
echo "done"  
