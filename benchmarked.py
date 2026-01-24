import yfinance as yf
import streamlit as st

# Adding title to the website.
st.title("Project: Benchmaked")
st.subheader("Does Nifty50 actually helps us?")


df = yf.download('^NSEI', start='2020-01-01', end='2026-01-20')

# Sidebar
sip_amount = st.sidebar.number_input("Monthly SIP Amount", min_value=500,value=5000 )

# Remove double column names.
df.columns = df.columns.get_level_values(0)

# Display data in a table
st.write("### Raw Market Data")
st.dataframe(df.head())

# Display a line chart
st.write('Nifty 50 closing price trend')
st.line_chart(df['Close'])

# move date from index to normal column
df = df.reset_index()
# Temproray column to identify month and year
df['Month_Year'] = df['Date'].dt.to_period('M')

sip_df = df.groupby('Month_Year').first().reset_index()
st.dataframe(sip_df.head())

sip_df['units_bought'] = sip_amount / sip_df['Close']
sip_df['Total_Units'] = sip_df['units_bought'].cumsum()
sip_df['portfolio_value'] = sip_df['Total_Units'] * sip_df['Close']

st.write("Your Portfolio Growth Over Time")
st.line_chart(sip_df.set_index('Date')['portfolio_value'])

# calucluate the total months of investment

# 1. Calculate the single number for total money put in
total_invested_final = len(sip_df) * sip_amount

# 2. Grab the single number for what it's worth now
current_value_final = sip_df['portfolio_value'].iloc[-1]

# 3. Just display them
st.write(f"Total Invested: ₹{total_invested_final:,.0f}")
st.write(f"Today's Value: ₹{current_value_final:,.0f}")