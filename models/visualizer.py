from pandas import DataFrame
import plotly.graph_objects as go

def plot_candlestick(data:DataFrame):
    """Function to plot candlestick chart.

    Parameters
    ----------
    data : DataFrame
        DataFrame containing the data with 'Open', 'High', 'Low', 'Close', 'Date' columns.
    """
    fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                                         open=data['Open'],
                                         high=data['High'],
                                         low=data['Low'],
                                         close=data['Close'])])
    fig.update_layout(title='Candlestick Chart', xaxis_title='Date', yaxis_title='Price')
    return fig

def plot_ema(data:DataFrame):
    """Function to plot Exponential Moving Averages.

    Parameters
    ----------
    data : DataFrame
        DataFrame containing the data with 'ema_10', 'ema_40', 'sma_200', 'Date' columns.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['ema_10'], mode='lines', name='EMA 10'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['ema_40'], mode='lines', name='EMA 40'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['sma_200'], mode='lines', name='SMA 200'))
    fig.update_layout(title='Exponential Moving Averages', xaxis_title='Date', yaxis_title='Value')
    return fig

def plot_levels(data:DataFrame):
    """Function to plot support and resistance levels.

    Parameters
    ----------
    data : DataFrame
        DataFrame containing the data with '52week_high', '52week_low', '20week_high', '20week_low', 'Date' columns.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['52week_high'], mode='lines', name='52 Week High'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['52week_low'], mode='lines', name='52 Week Low'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['20week_high'], mode='lines', name='20 Week High'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['20week_low'], mode='lines', name='20 Week Low'))
    fig.update_layout(title='Support and Resistance Levels', xaxis_title='Date', yaxis_title='Value')
    return fig

def plot_rsi(data:DataFrame):
    """Function to plot Relative Strength Index.

    Parameters
    ----------
    data : DataFrame
        DataFrame containing the data with 'rsi_14', 'rsi_7', 'Date' columns.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['rsi_14'], mode='lines', name='RSI 14'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['rsi_7'], mode='lines', name='RSI 7'))
    fig.update_layout(title='Relative Strength Index', xaxis_title='Date', yaxis_title='Value')
    return fig

def plot_trades(data:DataFrame, trades:DataFrame):
    """Function to plot trades on a candlestick chart.

    Parameters
    ----------
    data : DataFrame
        DataFrame containing the data with 'Open', 'High', 'Low', 'Close', 'Date' columns.
    trades : DataFrame
        DataFrame containing the trades with 'Date', 'Price', 'Type' columns.
    """
    fig = plot_candlestick(data)
    buy_trades = trades[trades['Type'] == 'buy']
    sell_trades = trades[trades['Type'] == 'sell']
    
    fig.add_trace(go.Scatter(x=buy_trades['Date'], y=buy_trades['Price'], mode='markers', name='Buy', marker=dict(color='green', symbol='triangle-up')))
    fig.add_trace(go.Scatter(x=sell_trades['Date'], y=sell_trades['Price'], mode='markers', name='Sell', marker=dict(color='red', symbol='triangle-down')))
    fig.update_layout(title='Trades on Candlestick Chart', xaxis_title='Date', yaxis_title='Price')
    return fig

def plot_balance(balance_history:DataFrame):
    """Function to plot balance over time.

    Parameters
    ----------
    balance_history : DataFrame
        DataFrame containing the balance history with 'Date' and 'Balance' columns.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=balance_history['Date'], y=balance_history['Balance'], mode='lines', name='Balance'))
    fig.update_layout(title='Account Balance Over Time', xaxis_title='Date', yaxis_title='Balance')
    return fig
