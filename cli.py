# cli.py
from bot import BasicBot, API_KEY, API_SECRET

def main():
    bot = BasicBot(API_KEY, API_SECRET)

    print("=== Binance Futures Testnet Trading Bot ===")
    symbol = input("Enter symbol (e.g., BTCUSDT): ").strip().upper()
    side = input("Side (BUY/SELL): ").strip().upper()
    order_type = input("Type (MARKET/LIMIT/STOP-LIMIT): ").strip().upper()
    quantity = float(input("Quantity: "))

    if order_type == "MARKET":
        result = bot.place_market_order(symbol, side, quantity)
    elif order_type == "LIMIT":
        price = input("Limit Price: ").strip()
        result = bot.place_limit_order(symbol, side, quantity, price)
    elif order_type == "STOP-LIMIT":
        stop_price = input("Stop Price: ").strip()
        limit_price = input("Limit Price: ").strip()
        result = bot.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)
    else:
        print("Invalid order type.")
        return

    print("\n=== ORDER RESULT ===")
    print(result)

if __name__ == "__main__":
    main()
