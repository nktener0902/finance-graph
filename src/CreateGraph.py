#!/usr/bin/env python
# coding: utf-8

import boto3
import pandas as pd
import urllib.request
import requests
import json
import io
import matplotlib.pyplot as plt
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from IPython.display import Image, display_png
import os


def lambda_handler(event, context):
    csv_string = get_csv()
    df = create_dataframe(csv_string)
    df_to_plot = extract_data_to_plot(df)
    create_fig(df_to_plot)
    response = send_fig_to_slack()
    return response


def get_csv(url=os.environ['URL']) -> str:
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    decoded_body = body.decode('utf-8-sig')
    return decoded_body


def create_dataframe(csv_string) -> pd.DataFrame:
    table_str = '\n'.join(csv_string.split('\n')[1:])
    return pd.read_csv(io.StringIO(table_str))


def extract_data_to_plot(table_dataframe):
    table_to_plot = pd.DataFrame({
        "time": pd.to_datetime(table_dataframe['基準日'], format='%Y/%m/%d'),
        "value": table_dataframe['基準価額（円）'],
        "value_containing_dividend": table_dataframe['分配金込み基準価額（円）']
    })
    return table_to_plot[(datetime.today() - relativedelta(months=6)) < table_to_plot['time']]


def create_fig(table_to_plot) -> None: 
    fig = plt.figure().add_subplot(1,1,1)
    fig.plot(table_to_plot['time'], table_to_plot['value'])
    plt.xticks(rotation=90)
    plt.savefig('trend.png')


def send_fig_to_slack() -> str:
    url = 'https://slack.com/api/files.upload'
    files = {'file': open('trend.png', 'rb')}
    params = {
        "token": os.environ['TOKEN'],
        "channels": os.environ['CHANNELS']
    }
    response = requests.post(url, files=files, params=params)

if __name__ == '__main__':
    lambda_handler(None, None)
