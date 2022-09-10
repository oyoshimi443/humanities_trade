import ccxt
from pprint import pprint
 
bitflyer = ccxt.bitflyer()

#Bitflyerで出来ることを確認しておく
#出力
pprint(bitflyer.has)


#取引所で取り扱っている通貨情報の取得
markets = bitflyer.load_markets() 
#出力
pprint(markets)


#板情報の取得
ticker = bitflyer.fetch_ticker(symbol='BTC/JPY')
#出力
pprint(ticker)


#板情報＋注文量の取得
orderbook = bitflyer.fetchOrderBook(symbol="BTC/JPY")
#出力
pprint(orderbook)


#ローソク足の取得
candles = bitflyer.fetch_ohlcv(symbol='BTC/JPY',     # 暗号資産[通貨]
                           timeframe = '15m',    # 時間足('1m', '5m', '1h', '1d')
                           since=None,           # 取得開始時刻(Unix Timeミリ秒)
                           limit=None,           # 取得件数(デフォルト:100、最大:500)
                           params={}             # 各種パラメータ
                          )

#出力
pprint(candles)