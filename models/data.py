import yfinance as yf
import pandas as pd
from pandas import DataFrame

def fetch_data(symbol:str ="EURUSD=X", start_date:str ="2020-01-01") -> DataFrame :
    data = yf.download(symbol, start=start_date)
    return data
