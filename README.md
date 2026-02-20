# Binance Futures Testnet Trading Bot

## Features
- Market and Limit orders
- BUY / SELL support
- CLI input
- Logging
- Error handling

## Setup
1. Clone repo
2. Create virtual environment
3. pip install -r requirements.txt
4. Add .env with API keys

## Run Examples

Market:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000

## Assumptions
- USDT-M Futures Testnet
- GTC used for LIMIT orders