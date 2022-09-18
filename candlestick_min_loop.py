## ループ処理で１分足の価格データを取得する ##
import requests
from datetime import datetime
import time

while True:
	response = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcfxjpy/ohlc?periods=60")
	response = response.json()

	data = response["result"]["60"][-2]

	close_time = datetime.fromtimestamp(data[0]).strftime('%Y/%m/%d %H:%M')
	open_price = data[1]
	close_price = data[4]

	print( "時間： " + close_time
		+ " 始値： " + str(open_price)
		+ " 終値： " + str(close_price) )

	time.sleep(15)