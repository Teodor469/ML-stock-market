import numpy as np
import pandas as pd
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


def fetch_stock_data(ticker):
    stock_data = yf.Ticker(ticker)
    return stock_data

msft = fetch_stock_data("MSFT")

print(msft.history(period="1mo"))