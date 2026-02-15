from fastapi import FastAPI
import ccxt

app = FastAPI()

# Bybit tiene una infraestructura muy amigable con servidores en la nube
exchange = ccxt.bybit()

@app.get("/")
def home():
    return {"status": "Conectado a Bybit Data Stream (BTC/USDT)"}

@app.get("/market-data")
def get_crypto_data(symbol: str = "BTC/USDT"):
    try:
        # Obtenemos el ticker (precio actual y variaciones)
        ticker = exchange.fetch_ticker(symbol)
        return {
            "symbol": symbol,
            "price": ticker['last'],
            "high_24h": ticker['high'],
            "low_24h": ticker['low'],
            "change_24h": ticker['percentage']
        }
    except Exception as e:
        return {"error": f"Fallo en Bybit: {str(e)}"}
