from fastapi import FastAPI
import ccxt

app = FastAPI()

# Configuramos Binance para usar el dominio de datos alternativo que suele evitar el bloqueo 451
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
        # Forzamos la carga de mercados para asegurar la conexión
        exchange.load_markets()
        ticker = exchange.fetch_ticker(symbol)
        return {
            "symbol": symbol,
            "price": ticker['last'],
            "high_24h": ticker['high'],
            "low_24h": ticker['low'],
            "change_24h": ticker['percentage']
        }
    except Exception as e:
        return {"error": f"Intento fallido con dominio de datos: {str(e)}"}
