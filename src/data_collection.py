#Separate file for scraping data from yfinance

import yfinance as yf


def fetch_stock_data(ticker):
    stock_data = yf.Ticker(ticker)
    return stock_data

msft = fetch_stock_data("MSFT")

print(msft.history(period="1mo"))