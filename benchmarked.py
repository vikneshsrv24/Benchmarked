import yfinance as yf
import streamlit as st

# Adding title to the website.
st.title("Project: Benchmaked")
st.subheader("Does Nifty50 actually helps us?")

df = yf.download('^NSEI', start='2020-01-01', end='2025-01-01')

# Display data in a table
st.write("### Raw Market Data")
st.dataframe(df.head())

# Display a line chart
st.write('Nifty 50 closing price trend')
st.line_chart(df['Close'])