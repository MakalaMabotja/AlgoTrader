import pandas as pd
import pandas_ta as ta
import numpy as np

"""
    Here we want to define the indicators class with the 3 types being numerical indicators(moving averages, RSI, BBands, etc),
    Levels(resistance & support), candles(candle stick patterns)
    
    For the Numeric indicators we will be using EMA_10, EMA_40, SMA_200 on the daily data, RSI 14 & 7, BBands (or ATR to use for SL/TP)
    For the Levels indicators we will be defining the global R/S levels as 52 week high/lows and the local levels to be 20 week levels
    For Candles we will define 12 candle stick patters, with 1,2,3 candle stick arguments
    -> i.e first checks if current candle is an indicator, then checks previous candle to see if there is a pattern
    -> if previous candle forms a 2 candle pattern then returns BULLISH/BEARING else it'll look one before to see if 
    -> the 2 previous candles form a pattern that aligns with the signal of the current candle or if a 3 candle pattern forms
    -> if no patter emerges then return NUETRAL
    
    -->technicalindicators\candlestick patterns cheatshee.txt
    
    _summary_
"""

class Indicators:
    def __init__(self, data):
        self.data = data
        self.numerical()
        self.levels()
        self.candlestick_patterns()

    def numerical(self):
        # Calculate numerical indicators
        self.data['ema_10'] = ta.ema(self.data['Close'], length=10)
        self.data['ema_40'] = ta.ema(self.data['Close'], length=40)
        self.data['sma_200'] = ta.sma(self.data['Close'], length=200)
        self.data['rsi_14'] = ta.rsi(self.data['Close'], length=14)
        self.data['rsi_7'] = ta.rsi(self.data['Close'], length=7)

        # Calculate moving average trends and RSI states
        self.calculate_mva_trend()
        self.calculate_rsi_state()

    def calculate_mva_trend(self):
        self.data['mva_trend'] = 'Neutral'
        for row in range(len(self.data)):
            if np.isnan(self.data['sma_200'].iloc[row]):
                self.data.loc[row, 'mva_trend'] = self.data['mva_trend'].iloc[row]
            else:
                condition = (self.data['Close'].iloc[row] > self.data['sma_200'].iloc[row]) or (self.data['ema_40'].iloc[row] > self.data['sma_200'].iloc[row])
                self.data.loc[row, 'mva_trend'] = "Bullish" if condition else "Bearish"

    def calculate_rsi_state(self):
        self.data['rsi_state'] = 'Neutral'
        for row in range(len(self.data)):
            condition1 = (self.data['rsi_14'].iloc[row] > 70)
            condition2 = (self.data['rsi_14'].iloc[row] < 30)
            if condition1:
                self.data.loc[row, 'rsi_state'] = "Overbought"
            elif condition2:
                self.data.loc[row, 'rsi_state'] = "Oversold"
            else:
                self.data.loc[row, 'rsi_state'] = "Neutral"

    def levels(self):
        # Calculate support and resistance levels
        # Placeholder implementation, you can customize this part
        self.data['support'] = 0
        self.data['resistance'] = 0
        # Calculate 52-week high/low
        self.data['52week_high'] = self.data['High'].rolling(window=252).max()
        self.data['52week_low'] = self.data['Low'].rolling(window=252).min()
        # Calculate 20-week support/resistance levels
        self.data['20week_high'] = self.data['High'].rolling(window=100).max()
        self.data['20week_low'] = self.data['Low'].rolling(window=100).min()

    def candlestick_patterns(self):
        # Detect candlestick patterns
        # Placeholder implementation, you can customize this part
        self.data['candlestick_pattern'] = 'Neutral'
        # Add logic to detect candlestick patterns
    
    def get_data(self):
        return self.data

