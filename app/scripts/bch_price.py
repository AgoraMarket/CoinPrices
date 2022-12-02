from pycoingecko import CoinGeckoAPI

from app import db
from app.classes.wallet_bch import Bch_Prices


def get_prices_coins_bch():
    """
    used pycoingecko modules for prices
    """
    cg = CoinGeckoAPI()

    # USD
    bch_data_usd = Bch_Prices.query.filter_by(id=1).first()
    bch_usd = cg.get_price(ids='bitcoin-cash', vs_currencies='usd')
    btc_cash_price_usd = (bch_usd['bitcoin-cash']['usd'])
    bch_data_usd.price = btc_cash_price_usd
    db.session.add(bch_data_usd)
    # EUR
    bch_data_eur = Bch_Prices.query.filter_by(id=2).first()
    bch_eur = cg.get_price(ids='bitcoin-cash', vs_currencies='eur')
    btc_cash_price_eur = (bch_eur['bitcoin-cash']['eur'])
    bch_data_eur.price = btc_cash_price_eur
    db.session.add(bch_data_eur)
    # JPY
    bch_data_jpy = Bch_Prices.query.filter_by(id=3).first()
    bch_jpy = cg.get_price(ids='bitcoin-cash', vs_currencies='jpy')
    btc_cash_price_jpy = (bch_jpy['bitcoin-cash']['jpy'])
    bch_data_jpy.price = btc_cash_price_jpy
    db.session.add(bch_data_jpy)
    # CAD
    bch_data_cad = Bch_Prices.query.filter_by(id=4).first()
    bch_cad = cg.get_price(ids='bitcoin-cash', vs_currencies='cad')
    btc_cash_price_cad = (bch_cad['bitcoin-cash']['cad'])
    bch_data_cad.price = btc_cash_price_cad
    db.session.add(bch_data_cad)
    # GBP
    bch_data_gbp = Bch_Prices.query.filter_by(id=5).first()
    bch_gbp = cg.get_price(ids='bitcoin-cash', vs_currencies='gbp')
    btc_cash_price_gbp = (bch_gbp['bitcoin-cash']['gbp'])
    bch_data_gbp.price = btc_cash_price_gbp
    db.session.add(bch_data_gbp)
    
    
    db.session.commit()

