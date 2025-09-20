import requests
import os
import csv
import time
from dotenv import load_dotenv
load_dotenv()

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
LIMIT = 1000

def run_stock_job(): 
    url = f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}'
    response = requests.get(url)
    tickers = []

    data = response.json()
    for ticker in data['results']:
        tickers.append(ticker)

    # get data from next url
    while ('next_url' in data):
        print('requesting next page', data['next_url'])
        time.sleep(10) # introduce a delay to avoid rate limiting

        response = requests.get(data['next_url'] + f'&apiKey={POLYGON_API_KEY}')
        data = response.json()
        print(data)
        for ticker in data['results']:
            tickers.append(ticker)

    example_ticker = {'ticker': 'HTRB', 
            'name': 'Hartford Total Return Bond ETF', 
            'market': 'stocks', 
            'locale': 'us', 
            'primary_exchange': 'ARCX', 
            'type': 'ETF', 
            'active': True, 
            'currency_name': 'usd', 
            'cik': '0001501825', 
            'composite_figi': 'BBG00HTN2K30', 
            'share_class_figi': 'BBG00HTN2KT2', 
            'last_updated_utc': '2025-09-17T15:54:25.562520983Z'}

    # write tickers to CSV - AI generated code
    columns = example_ticker.keys()
    with open('tickers.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        for t in tickers:
            row = {col: t.get(col, None) for col in columns}
            writer.writerow(row)

    print(f'Wrote {len(tickers)} rows to tickers.csv')

if __name__ == "__main__":
    run_stock_job()