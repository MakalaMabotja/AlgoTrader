import pandas as pd
from pandas import DataFrame
import numpy as np

def trade_results(data: DataFrame, initial_balance: float = 10000) -> DataFrame:
    if not all(col in data.columns for col in ['signal', 'position', 'Close']):
        raise ValueError("DataFrame must contain 'signal', 'position', and 'Close' columns")

    trades_list = []
    current_trade = 1
    entry_price = 0
    entry_date = None
    balance = initial_balance

    for row in range(1, len(data)):
        signal_diff = data['signal'].iloc[row] - data['signal'].iloc[row - 1]

        if signal_diff == 1 and data['position'].iloc[row - 1] == 'Closed':
            entry_price = data['Close'].iloc[row]
            entry_date = data.index[row]
        elif signal_diff == -1 and data['position'].iloc[row - 1] == 'Closed':  # Open Short Position
            entry_price = data['Close'].iloc[row]
            entry_date = data.index[row]
        elif signal_diff == -1 and data['position'].iloc[row - 1] == 'Long':  # Close Long Position
            exit_price = data['Close'].iloc[row]
            exit_date = data.index[row]
            trade_value = exit_price - entry_price
            trade_result = 'Success' if trade_value > 0 else 'Fail'
            balance += trade_value
            trades_list.append({
                'trade': current_trade,
                'entry_date': entry_date,
                'entry_price': entry_price,
                'exit_date': exit_date,
                'exit_price': exit_price,
                'position': 'Long',
                'value': trade_value,
                'result': trade_result,
                'balance': balance
            })
            current_trade += 1
        elif signal_diff == 1 and data['position'].iloc[row - 1] == 'Short':  # Close Short Position
            exit_price = data['Close'].iloc[row]
            exit_date = data.index[row]
            trade_value = entry_price - exit_price
            trade_result = 'Success' if trade_value > 0 else 'Fail'
            balance += trade_value
            trades_list.append({
                'trade': current_trade,
                'entry_date': entry_date,
                'entry_price': entry_price,
                'exit_date': exit_date,
                'exit_price': exit_price,
                'position': 'Short',
                'value': trade_value,
                'result': trade_result,
                'balance': balance
            })
            current_trade += 1

    trades_df = pd.DataFrame(trades_list)
    return trades_df

def trade_summary(data: DataFrame) -> DataFrame:
    summary = data.groupby(['position', 'result']).agg(
        total_value=pd.NamedAgg(column='value', aggfunc='sum'),
        average_value=pd.NamedAgg(column='value', aggfunc='mean'),
        percentage_of_total=pd.NamedAgg(column='value', aggfunc=lambda x: len(x) / len(data) * 100)
    ).reset_index()
    return summary

