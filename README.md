# Simplified Binance Futures Trading Bot

This is a command-line based trading bot built using Python and the Binance Futures **Testnet**. It allows users to place market and limit orders, including support for advanced order types like Stop and Stop-Limit.

## ✅ Features

- Place **Market** and **Limit** orders on Binance Futures Testnet (USDT-M)
- Support for **BUY** and **SELL** sides
- Support for advanced order types: **STOP_MARKET**, **STOP (Stop-Limit)**
- Uses **official Binance API** via `python-binance` SDK
- CLI-based interaction with **input validation**
- Logs API requests, responses, and errors to `trading_bot.log`
- Uses environment variables for API key/secret via `.env` file

## 🏁 Getting Started

### 1. Clone and Setup

unzip trading_bot.zip
cd trading_bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` to insert your **Binance Testnet** API credentials:

```
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

### 2. Example Usage

# Market Order (Buy)
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

# Limit Order (Sell)
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 66000

# Stop-Limit Order (Buy)
python main.py --symbol BTCUSDT --side BUY --type STOP --quantity 0.001 --price 67000 --stop_price 66500

# Stop-Market Order (Sell)
python main.py --symbol BTCUSDT --side SELL --type STOP_MARKET --quantity 0.001 --stop_price 66200
```

## 📁 Files

- `main.py`: CLI interface for placing orders
- `basic_bot.py`: Core logic and Binance API integration
- `requirements.txt`: Python dependencies
- `.env.example`: Template for storing Binance API credentials
- `trading_bot.log`: Log file for API requests and errors

## 📘 Notes

- Ensure you're using [Binance Futures Testnet](https://testnet.binancefuture.com) and credentials from the testnet dashboard.
- Only use small quantity values to avoid testnet rejections.

---

Developed for the Application Task: Simplified Binance Trading Bot
