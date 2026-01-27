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
    # Removeing unwanted rowns from the source itself.
    #data = data.drop(columns=['Volume','Open','High','Low','Adj Close'], errors='ignore')
    # Return only date without 00:00:00
    data['Date'] = data['Date'].dt.date
    return data[['Date','Close']]

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
    max_value=today,
    format="DD-MM-YYYY"
)
# End Date
end_date = st.sidebar.date_input(
    "End Date",
    value = today,
    min_value=before_ten_years,
    max_value=today,
    format="DD-MM-YYYY"
)


df =get_data("^NSEI", start_date, end_date)
st.subheader(f"{start_date} -- {end_date}")
# We are slicing the YYYY-MM-DD to YYYY-MM for better visulaization. 
df['Month_Year'] = df['Date'].astype(str).str[0:7]
# Now we will be grouping the months --> ?

# Cuz we have to find what if the user invested or SIP's in 1st of every month for a duration.
sip_df = df.groupby('Month_Year').first().reset_index()
# st.write(f"Original rows: {len(df)}")
# st.write(f"SIP rows: {len(sip_df)}")

# SIP CALCULATION
# 1. We will calculate the number of units bought for price / month.
sip_df['Units'] = sip_amount/sip_df['Close']  # Units bought per month.

# 2. Find Total Units.
sip_df['Total_Units'] = sip_df['Units'].cumsum()

# 3. Current value
sip_df['Portfoilo_value'] = sip_df['Total_Units'] *sip_df['Close']

# 4. Total Invested Amount
sip_df['Monthly_Investment'] = sip_amount
sip_df['Invested_amount'] = sip_df['Monthly_Investment'].cumsum()

# st.dataframe(df.head(), width='stretch')

st.markdown("----")

total_invested = sip_df['Invested_amount'].iloc[-1]
current_val = sip_df['Portfoilo_value'].iloc[-1]
profit = current_val - total_invested

return_pct = (profit/total_invested) * 100

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Invested", f"₹{total_invested:,.0f}")
col2.metric("📈 Current Value", f"₹{current_val:,.0f}")
col3.metric("🚀 Absolute Profit", f"₹{profit:,.0f}", delta=f"{return_pct:.1f}%")


# --- BLOCK 7: THE WEALTH CHART ---
st.subheader("Index Chart 🎯")

# We need to set the Date as the "Index" so the chart uses it for the X-axis
chart_data = sip_df.set_index('Date')[['Invested_amount', 'Portfoilo_value']]

# Plot it
st.line_chart(chart_data)