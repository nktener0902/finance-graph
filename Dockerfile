FROM lambci/lambda:build-python3.7

COPY Pipfile .
COPY packaging.sh .
RUN chmod +x packaging.sh

RUN sh packaging.sh

CMD cp lambbda_layer.zip /share
