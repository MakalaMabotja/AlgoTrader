import pandas as pd
from pandas import DataFrame
import pandas_ta as ta

class Indicator():
    def __init__ (self, data: DataFrame):
        self.data = data
        self.data = self.get_ema(self.data)
        self.data = self.get_rsi(self.data)
        self.data = self.get_levels(self.data)
        
    def get_ema(self, data: DataFrame) -> DataFrame:
        """Function for calculating exponential moving averages

        Parameters
        ----------
        data : DataFrame
            Data used for the ema calculation
        """
        data['ema_10'] = ta.ema(data['Close'], length=10)
        data['ema_40'] = ta.ema(data['Close'], length=40)
        data['sma_200'] = ta.sma(data['Close'], length=200)
        return data
        
    def get_rsi(self, data: DataFrame) -> DataFrame:
        """Function for calculating relative strength index

        Parameters
        ----------
        data : DataFrame
            Data used for the rsi calculation
        """
        data['rsi_14'] = ta.rsi(data['Close'], length=14)
        data['rsi_7'] = ta.rsi(data['Close'], length=7)
        return data
    
    def get_levels(self, data: DataFrame) -> DataFrame:
        """Function for calculating support and resistance levels

        Parameters
        ----------
        data : DataFrame
            Data used for the levels calculation
        """
        data['52week_high'] = data['High'].rolling(window=252).max()
        data['52week_low'] = data['Low'].rolling(window=252).min()
        data['20week_high'] = data['High'].rolling(window=100).max()
        data['20week_low'] = data['Low'].rolling(window=100).min()
        return data

