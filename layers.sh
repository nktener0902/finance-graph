#!/bin/bash  

mkdir dist-requests  
pip install -t ./dist-requests requests
zip -r requests.zip ./dist-requests/*

mkdir dist-pandas  
pip install -t ./dist-pandas pandas
zip -r pandas.zip ./dist-pandas/*

mkdir dist-matplotlib  
pip install -t ./dist-matplotlib matplotlib
zip -r matplotlib.zip ./dist-matplotlib/*

echo "done"  
