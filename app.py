<<<<<<< HEAD
import streamlit as st
import yfinance as yf
import pandas as pd

from indicators.technical_indicators import Indicator
from indicators.signals import Signals

from models.data import fetch_data
from models.visualizer import plot_candlestick, plot_ema, plot_levels, plot_rsi, plot_trades, plot_balance

# Load data
=======
# mainapp.py

import pandas as pd
import matplotlib.pyplot as plt
from technicalindicators.indicators import generate_indicators
from technicalindicators.signals import generate_all_signals

# Load data
def load_data():
    # Assuming you have a CSV file with columns: Date, Open, High, Low, Close
    data = pd.read_csv('eurusd\EURUSD_Daily_200001030000_201912310000.csv', parse_dates=['Date'])
    return data

# Visualize signals
def visualize_signals(data):
    # Plot prices
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Close'], label='Close Price', color='black')

    # Plot signals
    for column in data.columns:
        if 'signal' in column:
            plt.scatter(data['Date'][data[column] == 1], data['Close'][data[column] == 1], label=column)

    # Customize plot
    plt.title('Price and Signals')
    plt.legend()
    plt.show()
>>>>>>> 1ee8714e148ea0d48c77fb7edd3a6d37cf26e372

# Main script
if __name__ == "__main__":
    # Step 1: Load data
<<<<<<< HEAD
    data = fetch_data()

    # Step 2: Calculate technical indicators
    data = Indicator(data).data.reset_index()

        # Streamlit UI
    st.title('Algorithmic Trading Dashboard')

    # st.subheader('Candlestick Chart')
    st.plotly_chart(plot_candlestick(data))

    # st.subheader('Exponential Moving Averages')
    st.plotly_chart(plot_ema(data))

    # st.subheader('Support and Resistance Levels')
    st.plotly_chart(plot_levels(data))

    # st.subheader('Relative Strength Index')
    st.plotly_chart(plot_rsi(data))

    # st.subheader('Trades')
    # st.plotly_chart(plot_trades(data, trades))

    # st.subheader('Account Balance Over Time')

=======
    price_data = load_data()

    # Step 2: Calculate technical indicators
    price_data = generate_indicators(price_data)

    # Step 3: Generate signals
    price_data = generate_all_signals(price_data)

    # Step 4: Visualize signals
    visualize_signals(price_data)
    
print(price_data.head(5))

# mainapp.py

import pandas as pd
import matplotlib.pyplot as plt
from technicalindicators.indicators import generate_indicators
from technicalindicators.signals import generate_all_signals

# Load data
def load_data():
    # Assuming you have a CSV file with columns: Date, Open, High, Low, Close
    data = pd.read_csv('eurusd\EURUSD_Daily_200001030000_201912310000.csv', parse_dates=['Date'])
    return data

# Visualize signals
def visualize_signals(data):
    # Plot prices
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Close'], label='Close Price', color='black')

    # Plot signals
    for column in data.columns:
        if 'signal' in column:
            plt.scatter(data['Date'][data[column] == 1], data['Close'][data[column] == 1], label=column)

    # Customize plot
    plt.title('Price and Signals')
    plt.legend()
    plt.show()

# Main script
if __name__ == "__main__":
    # Step 1: Load data
    price_data = load_data()

    # Step 2: Calculate technical indicators
    price_data = generate_indicators(price_data)

    # Step 3: Generate signals
    price_data = generate_all_signals(price_data)

    # Step 4: Visualize signals
    visualize_signals(price_data)
    
print(price_data.head(5))
>>>>>>> 1ee8714e148ea0d48c77fb7edd3a6d37cf26e372
