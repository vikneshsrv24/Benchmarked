import yfinance as yf
import streamlit as st
import datetime as dt
import pandas as pd

# Adding title to the website.
st.set_page_config(
    page_title="Benchmarked",
    layout="wide",
    initial_sidebar_state="auto",
    page_icon="📈",
    )

st.title("Does Nifty50 actually helps us?")

# Caching the downloaded data
@st.cache_data()
def get_data(ticker,start,end):
    data = yf.download(ticker, start=start, end=end)

    # Remove double column names.
    data.columns = data.columns.get_level_values(0)
    data = data.reset_index()

    return data

st.sidebar.header("Investment Settings")
sip_amount = st.sidebar.slider(
    "Monthly SIP",
    min_value=500,
    max_value=100000,
    step=500
    )

# adding last 10 years of data.
today = dt.date.today()
before_ten_years = today - dt.timedelta(10*365)

# Start Date
start_date = st.sidebar.date_input(
    "Start Date",
    value = before_ten_years,
    min_value=dt.date(2000,1,1),
    max_value=today
)
# End Date
end_date = st.sidebar.date_input(
    "End Date",
    value = today,
    min_value=before_ten_years,
    max_value=today
)


