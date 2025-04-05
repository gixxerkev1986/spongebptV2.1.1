import requests
import pandas as pd
import pandas_ta as ta

def fetch_ohlc(symbol: str, interval: str = "1h", limit: int = 100) -> pd.DataFrame:
    url = f"https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbol.upper(),
        "interval": interval,
        "limit": limit
    }
    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data, columns=[
        "timestamp", "open", "high", "low", "close", "volume",
        "_", "_", "_", "_", "_", "_"
    ])
    df["close"] = pd.to_numeric(df["close"])
    df["open"] = pd.to_numeric(df["open"])
    df["high"] = pd.to_numeric(df["high"])
    df["low"] = pd.to_numeric(df["low"])
    df["volume"] = pd.to_numeric(df["volume"])
    return df

def analyse_multiple_timeframes(symbol: str) -> dict:
    timeframes = {
        "5m": "5m",
        "10m": "10m",
        "15m": "15m",
        "30m": "30m",
        "1h": "1h",
        "1d": "1d"
    }
    results = {}

    for label, tf in timeframes.items():
        df = fetch_ohlc(symbol, tf, limit=100)
        df["rsi"] = ta.rsi(df["close"], length=14)
        df["ema20"] = ta.ema(df["close"], length=20)
        df["ema50"] = ta.ema(df["close"], length=50)

        trend = "Bullish" if df["ema20"].iloc[-1] > df["ema50"].iloc[-1] else "Bearish"

        results[label] = {
            "rsi": df["rsi"].iloc[-1],
            "close": df["close"].iloc[-1],
            "trend": trend
        }
    return results