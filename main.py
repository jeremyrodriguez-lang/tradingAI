from fastapi import FastAPI
import ccxt

app = FastAPI()
exchange = ccxt.binance()

@app.get("/")
def home():
    return {"status": "Agente de Trading Conectado", "market": "Bitcoin"}

@app.get("/market-data")
def get_crypto_data(symbol: str = "BTC/USDT"):
    try:
        ticker = exchange.fetch_ticker(symbol)
        return {
            "symbol": symbol,
            "price": ticker['last'],
            "high_24h": ticker['high'],
            "low_24h": ticker['low'],
            "change_24h": ticker['percentage']
        }
    except Exception as e:
        return {"error": str(e)}
