import yfinance as yf
import pandas as pd

tickers = ["AAPL", "MSFT", "TSLA"]

def extract(tickers):
    stock_price = {ticker: yf.Ticker(ticker).history(period="5y") for ticker in tickers}
    print(stock_price)
    return stock_price

def transform(stock_price_dict):
    transformed_data = {}
    for ticker, df in stock_price_dict.items():
        # reset index to make 'Date' a column
        df_reset = df.reset_index()
        # keep only 'Date' and 'Close' columns
        transformed_df = df_reset[['Date', 'Close']].copy()
        # rename columns 
        transformed_df.rename(columns={'Close': 'Closing Price'}, inplace=True)
        # store in dictionary
        transformed_data[ticker] = transformed_df
        print(f"Transformed data for {ticker}:\n", transformed_df.head(), "\n")
    return transformed_data


def run_etl_pipeline():
    stock_prices = extract(tickers)

    transformed_stock_prices = transform(stock_prices)

    # print(transformed_stock_prices)

    # load()

run_etl_pipeline()