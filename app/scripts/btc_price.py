from pycoingecko import CoinGeckoAPI

from app import db
from app.classes.wallet_btc import Btc_Prices



def get_prices_coins_btc():
    cg = CoinGeckoAPI()
    # USD
    btc_data_usd = Btc_Prices.query.filter_by(id=1).first()
    btc_usd = cg.get_price(ids='bitcoin', vs_currencies='usd')
    btc_price_usd = (btc_usd['bitcoin']['usd'])
    btc_data_usd.price = btc_price_usd
    db.session.add(btc_data_usd)
    # EUR
    btc_data_eur = Btc_Prices.query.filter_by(id=2).first()
    btc_eur = cg.get_price(ids='bitcoin', vs_currencies='eur')
    btc_price_eur = (btc_eur['bitcoin']['eur'])
    btc_data_eur.price = btc_price_eur
    db.session.add(btc_data_eur)
    # JPY
    btc_data_jpy = Btc_Prices.query.filter_by(id=3).first()
    btc_jpy = cg.get_price(ids='bitcoin', vs_currencies='jpy')
    btc_price_jpy = (btc_jpy['bitcoin']['jpy'])
    btc_data_jpy.price = btc_price_jpy
    db.session.add(btc_data_jpy)
    # CAD
    btc_data_cad = Btc_Prices.query.filter_by(id=4).first()
    btc_cad = cg.get_price(ids='bitcoin', vs_currencies='cad')
    btc_cash_price_cad = (btc_cad['bitcoin']['cad'])
    btc_data_cad.price = btc_cash_price_cad
    db.session.add(btc_data_cad)
    # GBP
    btc_data_gbp = Btc_Prices.query.filter_by(id=5).first()
    btc_gbp = cg.get_price(ids='bitcoin', vs_currencies='gbp')
    btc_price_gbp = (btc_gbp['bitcoin']['gbp'])
    btc_data_gbp.price = btc_price_gbp
    db.session.add(btc_data_gbp)
    
if __name__ == '__main__':
    get_prices_coins_btc()
