from basic_bot import BasicBot
import argparse
import os
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser(description='Binance Futures Trading Bot')
parser.add_argument('--symbol', required=True, help='Trading pair symbol like BTCUSDT')
parser.add_argument('--side', required=True, choices=['BUY', 'SELL'], help='Order side')
parser.add_argument('--type', required=True, choices=['MARKET', 'LIMIT', 'STOP_MARKET', 'STOP'], help='Order type')
parser.add_argument('--quantity', required=True, type=float, help='Order quantity')
parser.add_argument('--price', type=float, help='Price for LIMIT or STOP order')
parser.add_argument('--stop_price', type=float, help='Stop price for STOP or STOP_MARKET order')
args = parser.parse_args()

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

bot = BasicBot(api_key, api_secret, testnet=True)
bot.place_order(args.symbol, args.side, args.type, args.quantity, args.price, args.stop_price)
