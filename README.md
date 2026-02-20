# Binance Futures Trading Bot (Testnet)

A simplified trading bot built using Python that places MARKET and LIMIT orders on Binance USDT-M Futures Testnet.

## Features

- Market Orders
- Limit Orders
- BUY and SELL support
- CLI-based input
- Structured architecture
- Logging of API requests and responses
- Exception handling

## Project Structure

trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── requirements.txt

## Setup

1. Clone repository
2. Create virtual environment
3. Install dependencies:

pip install -r requirements.txt

4. Create .env file:

BINANCE_API_KEY=your_key
BINANCE_API_SECRET=your_secret

## Example Usage

Market Order:

python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:

python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000

## Assumptions

- USDT-M Futures Testnet
- GTC used for LIMIT orders