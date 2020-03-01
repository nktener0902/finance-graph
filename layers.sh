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

echo "BUCKET_NAME is ${BUCKET_NAME}"
if [ -n "${BUCKET_NAME}" ]; then
  echo "Uploading archives to S3..."
  aws s3 cp requests.zip s3://${BUCKET_NAME}/requests.zip
  aws s3 cp pandas.zip s3://${BUCKET_NAME}/pandas.zip
  aws s3 cp matplotlib.zip s3://${BUCKET_NAME}/matplotlib.zip
fi

echo "done"  
