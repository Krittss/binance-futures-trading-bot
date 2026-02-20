import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_quantity
from bot.logging_config import setup_logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        client = get_client()

        response = place_order(
            client=client,
            symbol=args.symbol.upper(),
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=args.price
        )

        print("\n===== ORDER SUMMARY =====")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        print("\n===== RESPONSE =====")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")
        print("\n✅ Order placed successfully!")

    except Exception as e:
        print(f"\n❌ Failed: {str(e)}")

if __name__ == "__main__":
    main()