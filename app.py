import streamlit as st
import yfinance as yf
import pandas as pd

from indicators.technicals import Indicator
from indicators.signals import Signals

from models.data import fetch_data
from models.visualizer import plot_candlestick, plot_ema, plot_levels, plot_rsi, plot_trades, plot_balance

# Load data

# Main script
if __name__ == "__main__":
    # Step 1: Load data
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
    st.plotly_chart(plot_trades(data, trades))

    st.subheader('Account Balance Over Time')

