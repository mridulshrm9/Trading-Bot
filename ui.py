# ui.py
import streamlit as st
from bot import BasicBot, API_KEY, API_SECRET

bot = BasicBot(API_KEY, API_SECRET)

st.title("🟡 Binance Futures Trading Bot (Testnet)")

symbol = st.text_input("Trading Symbol", "BTCUSDT").upper()
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Order Type", ["MARKET", "LIMIT", "STOP-LIMIT"])
quantity = st.number_input("Quantity", min_value=0.001, format="%.6f")

price = None
stop_price = None
limit_price = None

if order_type == "LIMIT":
    price = st.text_input("Limit Price")
elif order_type == "STOP-LIMIT":
    stop_price = st.text_input("Stop Price")
    limit_price = st.text_input("Limit Price")

if st.button("Place Order"):
    if order_type == "MARKET":
        response = bot.place_market_order(symbol, side, quantity)
    elif order_type == "LIMIT":
        response = bot.place_limit_order(symbol, side, quantity, price)
    elif order_type == "STOP-LIMIT":
        response = bot.place_stop_limit_order(symbol, side, quantity, stop_price, limit_price)

    st.success("✅ Order Executed")
    st.json(response)
