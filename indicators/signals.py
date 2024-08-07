import pandas as pd
import numpy as np

class Signals:
    BUY = 1
    CLOSE = 0
    SELL = -1

    def __init__(self, data: pd.DataFrame):
        self.data = data
        # Initialize columns
        self.data['signal'] = self.CLOSE
        self.data['position'] = 'Closed'
        self.data['entry_price'] = 0.0
        self.data['exit_price'] = 0.0
        
        self.trade()
        self.position()

    def trade(self):
        self.data['signal'] = np.where(
            (self.data['mva_trend'] == 'Bullish') & (self.data['ema_10'] > self.data['ema_40']),
            self.BUY,
            np.where(
                (self.data['mva_trend'] == 'Bearish') & (self.data['ema_10'] < self.data['ema_40']),
                self.SELL,
                self.CLOSE
            )
        )

    def position(self):
        for row in range(1, len(self.data)):
            signal_diff = self.data['signal'].iloc[row] - self.data['signal'].iloc[row - 1]

            if signal_diff == 1 and self.data['position'].iloc[row - 1] == 'Closed':  # Open Long Position
                self.data.at[row, 'position'] = 'Long'
                self.data.at[row, 'entry_price'] = self.data['Close'].iloc[row]

            elif signal_diff == -1 and self.data['position'].iloc[row - 1] == 'Closed':  # Open Short Position
                self.data.at[row, 'position'] = 'Short'
                self.data.at[row, 'entry_price'] = self.data['Close'].iloc[row]

            elif signal_diff == -1 and self.data['position'].iloc[row - 1] == 'Long':  # Close Long Position
                self.data.at[row, 'position'] = 'Closed'
                self.data.at[row, 'exit_price'] = self.data['Close'].iloc[row]

            elif signal_diff == 1 and self.data['position'].iloc[row - 1] == 'Short':  # Close Short Position
                self.data.at[row, 'position'] = 'Closed'
                self.data.at[row, 'exit_price'] = self.data['Close'].iloc[row]
            
            else:
                self.data.at[row, 'position'] = self.data.at[row - 1, 'position']
                self.data.at[row, 'entry_price'] = self.data.at[row - 1, 'entry_price']
                self.data.at[row, 'exit_price'] = self.data.at[row - 1, 'exit_price']

    def get_data(self):
        return self.data
