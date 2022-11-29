from pycoingecko import CoinGeckoAPI

from app import db
from app.classes.wallet_xmr import Xmr_Prices

def get_prices_coins_xmr():
    cg = CoinGeckoAPI()
    # USD
    xmr_data_usd = Xmr_Prices.query.filter_by(id=1).first()
    xmr_usd = cg.get_price(ids='monero', vs_currencies='usd')
    xmr_price_usd = (xmr_usd['monero']['usd'])
    xmr_data_usd.price = xmr_price_usd
    db.session.add(xmr_data_usd)

    # EUR
    xmr_data_eur = Xmr_Prices.query.filter_by(id=2).first()
    xmr_eur = cg.get_price(ids='monero', vs_currencies='eur')
    xmr_price_eur = (xmr_eur['monero']['eur'])
    xmr_data_eur.price = xmr_price_eur
    db.session.add(xmr_data_eur)
    
    # JPY
    xmr_data_jpy = Xmr_Prices.query.filter_by(id=3).first()
    xmr_jpy = cg.get_price(ids='monero', vs_currencies='jpy')
    xmr_price_jpy = (xmr_jpy['monero']['jpy'])
    xmr_data_jpy.price = xmr_price_jpy
    db.session.add(xmr_data_jpy)
    
    # CAD
    xmr_data_cad = Xmr_Prices.query.filter_by(id=4).first()
    xmr_cad = cg.get_price(ids='monero', vs_currencies='cad')
    xmr_cash_price_cad = (xmr_cad['monero']['cad'])
    xmr_data_cad.price = xmr_cash_price_cad
    db.session.add(xmr_data_cad)
    
    # GBP
    xmr_data_gbp = Xmr_Prices.query.filter_by(id=5).first()
    xmr_gbp = cg.get_price(ids='monero', vs_currencies='gbp')
    xmr_price_gbp = (xmr_gbp['monero']['gbp'])
    xmr_data_gbp.price = xmr_price_gbp
    db.session.add(xmr_data_gbp)

if __name__ == '__main__':
    get_prices_coins_xmr()
