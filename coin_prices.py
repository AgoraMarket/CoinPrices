from pycoingecko import CoinGeckoAPI

from app import db
from app.classes.wallet_bch import Bch_Prices
from app.classes.wallet_btc import Btc_Prices
from app.classes.wallet_xmr import Xmr_Prices


def get_prices_coins_bch():
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

def get_prices_coins_btc():
    cg = CoinGeckoAPI()
    # USD
    btc_data_usd = Btc_Prices.query.filter_by(id=1).first()
    btc_usd = cg.get_price(ids='bitcoin', vs_currencies='usd')
    btc_price_usd = (btc_usd['bitcoin']['usd'])
    btc_data_usd.price = btc_price_usd
    db.session.add(btc_data_usd)
    # EUR
    btc_data_eur = Bch_Prices.query.filter_by(id=2).first()
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
    get_prices_coins_bch()
    get_prices_coins_btc()
    get_prices_coins_xmr()
    db.session.commit()