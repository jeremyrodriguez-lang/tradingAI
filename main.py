from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Conectado a Yahoo Finance (Global Stream)"}

@app.get("/market-data")
def get_crypto_data(symbol: str = "BTC-USD"):
    # Adaptamos el símbolo para Yahoo Finance
    ticker_symbol = "BTC-USD"
    
    try:
        # Obtenemos los datos del ticker
        data = yf.Ticker(ticker_symbol)
        info = data.fast_info
        history = data.history(period="1d")
        
        return {
            "symbol": "BTC/USDT",
            "price": info['last_price'],
            "high_24h": history['High'].iloc[-1],
            "low_24h": history['Low'].iloc[-1],
            "change_24h": ((info['last_price'] - info['open']) / info['open']) * 100
        }
    except Exception as e:
        return {"error": f"Error en la conexión global: {str(e)}"}
