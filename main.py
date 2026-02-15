from fastapi import FastAPI
import ccxt

app = FastAPI()

# Configuramos Binance para usar el dominio de datos alternativo
exchange = ccxt.binance({
    'urls': {
        'api': {
            'public': 'https://data.binance.com/api/v3',
        }
    }
})

@app.get("/")
def home():
    return {"status": "Conectado a Binance Data Stream"}

@app.get("/market-data")
def get_crypto_data(symbol: str = "BTC/USDT"):
    try:
        # Usamos fetch_ticker que es una llamada pública
        ticker = exchange.fetch_ticker(symbol)
        return {
            "symbol": symbol,
            "price": ticker['last'],
            "high_24h": ticker['high'],
            "low_24h": ticker['low'],
            "change_24h": ticker['percentage']
        }
    except Exception as e:
        return {"error": f"Binance sigue bloqueando: {str(e)}"}
