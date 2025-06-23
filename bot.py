# bot.py
import os
import logging
from dotenv import load_dotenv
from binance.um_futures import UMFutures  # Correct import

# Load .env values
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Logging setup
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BasicBot:
    def __init__(self, api_key, api_secret):
        self.client = UMFutures(key=api_key, secret=api_secret,
                                base_url="https://testnet.binancefuture.com")
        logging.info("Initialized Binance UMFutures client")

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.new_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type="MARKET",
                quantity=quantity
            )
            logging.info(f"Market order placed: {order}")
            return order
        except Exception as e:
            logging.error("Market order failed", exc_info=e)
            return {"error": str(e)}

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.new_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )
            logging.info(f"Limit order placed: {order}")
            return order
        except Exception as e:
            logging.error("Limit order failed", exc_info=e)
            return {"error": str(e)}

    def place_stop_limit_order(self, symbol, side, quantity, stop_price, limit_price):
        try:
            order = self.client.new_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type="STOP",
                timeInForce="GTC",
                quantity=quantity,
                stopPrice=stop_price,
                price=limit_price
            )
            logging.info(f"Stop-limit order placed: {order}")
            return order
        except Exception as e:
            logging.error("Stop-limit order failed", exc_info=e)
            return {"error": str(e)}
