import logging
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException

logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        try:
            if testnet:
                self.client = Client(api_key, api_secret, testnet=True)
                self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
            else:
                self.client = Client(api_key, api_secret)

            self.client.futures_account()
            logging.info("✅ Connected to Binance Futures Testnet.")
            print("✅ Connected to Binance Futures Testnet.")

        except BinanceAPIException as e:
            logging.error(f"Binance API error: {e}")
            raise SystemExit("❌ Failed to connect to Binance Testnet.")
        except Exception as e:
            logging.error(f"General connection error: {e}")
            raise SystemExit("❌ Unexpected error during connection.")

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            params = {
                'symbol': symbol,
                'side': SIDE_BUY if side == 'BUY' else SIDE_SELL,
                'type': order_type,
                'quantity': quantity
            }

            if order_type == ORDER_TYPE_LIMIT:
                if not price:
                    raise ValueError("Price required for LIMIT order.")
                params['price'] = price
                params['timeInForce'] = TIME_IN_FORCE_GTC

            elif order_type == ORDER_TYPE_STOP_MARKET:
                if not stop_price:
                    raise ValueError("Stop price required for STOP_MARKET order.")
                params['stopPrice'] = stop_price

            elif order_type == ORDER_TYPE_STOP:
                if not (price and stop_price):
                    raise ValueError("Price and Stop price required for STOP_LIMIT order.")
                params['stopPrice'] = stop_price
                params['price'] = price
                params['timeInForce'] = TIME_IN_FORCE_GTC

            elif order_type == ORDER_TYPE_MARKET:
                pass

            else:
                raise ValueError("Unsupported order type.")

            order = self.client.futures_create_order(**params)
            logging.info(f"✅ Order placed: {order}")
            print("✅ Order executed successfully.")
            return order

        except BinanceAPIException as e:
            logging.error(f"❌ Binance API error: {e}")
            print("❌ Binance API error. Check log for details.")
        except Exception as e:
            logging.error(f"❌ Unexpected error: {e}")
            print("❌ Unexpected error. Check log for details.")
