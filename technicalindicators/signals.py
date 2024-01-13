import pandas as pd
import pandas_ta as ta
import numpy as np

class Signals:
    BUY = 1
    CLOSE = 0
    SELL = -1

    def __init__(self, data):
        self.data = data  # Copy the DataFrame to avoid modifying the original
        self.trade()
        self.position()

    def trade(self):
        for row in range(len(self.data)):
            if self.data['mva_trend'].iloc[row] == 'Bullish':
                self.data['signal'].iloc[row] = np.where(self.data['ema_10'].iloc[row] > self.data['ema_40'].iloc[row], self.BUY, self.CLOSE)
            elif self.data['mva_trend'].iloc[row] == 'Bearish':
                self.data['signal'].iloc[row] = np.where(self.data['ema_10'].iloc[row] < self.data['ema_40'].iloc[row], self.SELL, self.CLOSE)
            else:
                self.data['signal'].iloc[row] = self.CLOSE

    def position(self):
        self.data['position'] = 'Closed'
        self.data['entry_price'] = 0
        self.data['exit_price'] = 0
        for row in range(1, len(self.data)):
            signal_diff = self.data['signal'].iloc[row] - self.data['signal'][row - 1]

            if signal_diff == 1 and self.data['position'][row - 1] == 'Closed':  # Open Long Position
                self.data.loc[row, 'position'] = 'Long'
                self.data.loc[row, 'entry_price'] = self.data['Close'].iloc[row]

            elif signal_diff == -1 and self.data['position'][row - 1] == 'Closed':  # Open Short Position
                self.data.loc[row, 'position'] = 'Short'
                self.data.loc[row, 'entry_price'] = self.data['Close'].iloc[row]

            elif signal_diff == -1 and self.data['position'][row - 1] == 'Long':  # Close Long Position
                self.data.loc[row, 'position'] = 'Closed'
                self.data.loc[row, 'exit_price'] = self.data['Close'].iloc[row]

            elif signal_diff == 1 and self.data['position'][row - 1] == 'Short':  # Close Short Position
                self.data.loc[row, 'position'] = 'Closed'
                self.data.loc[row, 'exit_price'] = self.data['Close'].iloc[row]
            
            else:
                self.data.loc[row, 'position'] = self.data.loc[row-1, 'position']
                self.data.loc[row, 'entry_price'] = self.data.loc[row-1, 'entry_price']
                self.data.loc[row, 'exit_price'] = self.data.loc[row-1, 'exit_price']

    def get_data(self):
        return self.data
