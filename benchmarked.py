import yfinance as yf

df = yf.download('^NSEI', start='2020-01-01', end='2025-01-01')

print(df.head())