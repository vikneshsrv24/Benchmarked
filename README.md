
# Benchmarked: Nifty 50 SIP Backtesting

### Project Overview

**Benchmarked** is a financial data analysis tool designed to backtest Systematic Investment Plans (SIP) against the Nifty 50 index.

Unlike standard calculators that use estimated annual returns, this application ingests historical market data to simulate real-world investment scenarios. It accounts for daily price fluctuations and executes "buys" on specific monthly dates to provide an accurate calculation of wealth accumulation over 10+ years.

### Key Features

* **Historical Data Integration:** Fetches real-time historical data using the Yahoo Finance API (`yfinance`), ensuring analysis is based on actual market performance rather than theoretical averages.
* **Accurate SIP Logic:** Utilizes Pandas time-series grouping to convert daily market data into monthly investment buckets, simulating a realistic "1st of the month" investment strategy.
* **Interactive Visualization:** Features a dynamic Plotly chart that visualizes the divergence between "Total Invested Capital" and "Current Portfolio Value" over time.
* **Vectorized Calculation:** Leverages Pandas vectorization for efficient computation of unit accumulation, cumulative sums, and absolute returns.
* **Indian Market Context:** Tailored for Indian investors with INR currency formatting (Lakhs/Crores) and Nifty 50 benchmarking.

### Technical Stack 🎯

* **Language:** Python 3.12.6
* **Frontend:** Streamlit
* **Data Processing:** Pandas, NumPy
* **Data Source:** yfinance API
* **Visualization:** Plotly Express

### Installation & Usage

1. **Clone the repository:**
```bash
git clone https://github.com/vikneshsrv/benchmarked.git
cd benchmarked

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the application:**
```bash
streamlit run benchamrked.py

```



### Methodology

The engine follows a strict data pipeline:

1. **Ingestion:** Downloads daily OHLC data for the Nifty 50 index (`^NSEI`) for the user-defined date range.
2. **Resampling:** Resamples daily data to monthly frequency, selecting the first trading day of each month to simulate the SIP execution date.
3. **Computation:** Calculates the number of units bought per month based on the closing price (`Investment Amount / Closing Price`), then computes the cumulative value of the portfolio.

### License

This project is licensed under the MIT License.
