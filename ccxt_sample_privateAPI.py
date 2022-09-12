import ccxt
from pprint import pprint
 

# #APIキー＆シークレットキー
api_key = "APIキー"
api_secret = "APIシークレット"

# # #オブジェクト生成 ccxt.●●●●()の●●●●部分は取引所名を入力
base = ccxt.bitflyer({'apiKey':apiKey,'secret':secret})

# 口座残高の取得
balance = base.fetch_balance()
#出力
pprint(balance)


# 口座情報の取得
collateral = base.private_get_getcollateral()
#出力
pprint( collateral )


# 買い注文
order = base.create_order(
	symbol = 'BTC/JPY', #通過
	type='limit',       #注文方法：market(成行)、limit(指値)
	side='buy',         #指値の場合価格を指定
	price='2815000',    #購入(buy) or 売却(sell)
	amount='0.01',      #購入数量
	params = { "product_code" : "FX_BTC_JPY" })
#出力
pprint(order)


# 注文状況の確認
orders = base.private_get_getchildorders(params = {"product_code" : "FX_BTC_JPY", "count" : 10}) 
for i in range(len(orders)):
    if orders[i]["child_order_state"] == "ACTIVE":
        pprint(orders[i]['child_order_acceptance_id'])


# 注文のキャンセル
#注文した際の'child_order_acceptance_id'
order_id = 'JRF20220911-043441-046295'
cancel_order = base.cancel_order(order_id, 'FX_BTC_JPY')
#出力
pprint(cancel_order)


# 注文内容をキャンセル（未約定の全注文）
orders = base.private_get_getchildorders(params = {"product_code" : "FX_BTC_JPY"})
for o in orders:
	bitflyer.cancel_order(
		symbol = "BTC/JPY",
		id = o["child_order_acceptance_id"],
		params = { "product_code" : "FX_BTC_JPY" })