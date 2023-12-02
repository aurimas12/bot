import yfinance as yf

def get_last_day_price(crypto_ticker):
    ticker = yf.Ticker(crypto_ticker)
    data = ticker.history(period="max")
    return data

x=get_last_day_price('ETH-USD')
print(x)