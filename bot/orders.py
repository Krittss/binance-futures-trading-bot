import logging
from binance.exceptions import BinanceAPIException, BinanceOrderException

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        elif order_type == "LIMIT":
            if price is None:
                raise ValueError("Price required for LIMIT order")

            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logging.info(f"Order response: {response}")
        return response

    except (BinanceAPIException, BinanceOrderException) as e:
        logging.error(f"Binance error: {e}")
        raise

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise