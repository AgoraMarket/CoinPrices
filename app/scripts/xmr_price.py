
from app import db
from app.classes.wallet_xmr import Xmr_Prices

def get_prices_coins_xmr(jsonprices):
    """
    used pycoingecko modules for prices
    """

    # USD
    xmr_price_usd = (jsonprices['monero']['usd'])
    xmr_data_usd = Xmr_Prices.query.filter_by(currency_id=0).first()
    xmr_data_usd.price = xmr_price_usd
    db.session.add(xmr_data_usd)

    # PHP
    xmr_price_php = (jsonprices['monero']['php'])
    xmr_data_php = Xmr_Prices.query.filter_by(currency_id=1).first()
    xmr_data_php.price = xmr_price_php
    db.session.add(xmr_data_php)

    #CHF
    xmr_price_chf = (jsonprices['monero']['chf'])
    xmr_data_chf = Xmr_Prices.query.filter_by(currency_id=2).first()
    xmr_data_chf.price = xmr_price_chf
    db.session.add(xmr_data_chf)

    # CAD
    xmr_price_cad = (jsonprices['monero']['cad'])
    xmr_data_cad = Xmr_Prices.query.filter_by(currency_id=3).first()
    xmr_data_cad.price = xmr_price_cad
    db.session.add(xmr_data_cad)
    
    # SGD
    xmr_price_sgd = (jsonprices['monero']['sgd'])
    xmr_data_sgd = Xmr_Prices.query.filter_by(currency_id=4).first()
    xmr_data_sgd.price = xmr_price_sgd
    db.session.add(xmr_data_sgd)
    
    # DKK
    xmr_price_dkk = (jsonprices['monero']['dkk'])
    xmr_data_dkk = Xmr_Prices.query.filter_by(currency_id=5).first()
    xmr_data_dkk.price = xmr_price_dkk
    db.session.add(xmr_data_dkk)
    
    # NOK
    xmr_price_nok = (jsonprices['monero']['nok'])
    xmr_data_nok = Xmr_Prices.query.filter_by(currency_id=6).first()
    xmr_data_nok.price = xmr_price_nok
    db.session.add(xmr_data_nok)

    # ILS
    xmr_price_ils = (jsonprices['monero']['ils'])
    xmr_data_ils = Xmr_Prices.query.filter_by(currency_id=7).first()
    xmr_data_ils.price = xmr_price_ils
    db.session.add(xmr_data_ils)


    # SEK
    xmr_price_sek = (jsonprices['monero']['sek'])
    xmr_data_sek = Xmr_Prices.query.filter_by(currency_id=8).first()
    xmr_data_sek.price = xmr_price_sek
    db.session.add(xmr_data_sek)

    # THB
    xmr_price_thb = (jsonprices['monero']['thb'])
    xmr_data_thb = Xmr_Prices.query.filter_by(currency_id=9).first()
    xmr_data_thb.price = xmr_price_thb
    db.session.add(xmr_data_thb)

    # BRL
    xmr_price_brl = (jsonprices['monero']['brl'])
    xmr_data_brl = Xmr_Prices.query.filter_by(currency_id=10).first()
    xmr_data_brl.price = xmr_price_brl
    db.session.add(xmr_data_brl)

    # INR
    xmr_price_inr = (jsonprices['monero']['inr'])
    xmr_data_inr = Xmr_Prices.query.filter_by(currency_id=11).first()
    xmr_data_inr.price = xmr_price_inr
    db.session.add(xmr_data_inr)

    # ZAR
    xmr_price_zar = (jsonprices['monero']['zar'])
    xmr_data_zar = Xmr_Prices.query.filter_by(currency_id=12).first()
    xmr_data_zar.price = xmr_price_zar
    db.session.add(xmr_data_zar)

    # HKD
    xmr_price_hkd = (jsonprices['monero']['hkd'])
    xmr_data_hkd = Xmr_Prices.query.filter_by(currency_id=13).first()
    xmr_data_hkd.price = xmr_price_hkd
    db.session.add(xmr_data_hkd)

    # JPY
    xmr_price_jpy = (jsonprices['monero']['jpy'])
    xmr_data_jpy = Xmr_Prices.query.filter_by(currency_id=14).first()
    xmr_data_jpy.price = xmr_price_jpy
    db.session.add(xmr_data_jpy)

    # HUF
    xmr_price_huf = (jsonprices['monero']['huf'])
    xmr_data_huf = Xmr_Prices.query.filter_by(currency_id=15).first()
    xmr_data_huf.price = xmr_price_huf
    db.session.add(xmr_data_huf)

    # MXN
    xmr_price_mxn = (jsonprices['monero']['mxn'])
    xmr_data_mxn = Xmr_Prices.query.filter_by(currency_id=16).first()
    xmr_data_mxn.price = xmr_price_mxn
    db.session.add(xmr_data_mxn)

    # CNY
    xmr_price_cny = (jsonprices['monero']['cny'])
    xmr_data_cny = Xmr_Prices.query.filter_by(currency_id=17).first()
    xmr_data_cny.price = xmr_price_cny
    db.session.add(xmr_data_mxn)

    # AUD
    xmr_price_aud = (jsonprices['monero']['aud'])
    xmr_data_aud = Xmr_Prices.query.filter_by(currency_id=18).first()
    xmr_data_aud.price = xmr_price_aud
    db.session.add(xmr_data_aud)

    # PLN
    xmr_price_pln = (jsonprices['monero']['pln'])
    xmr_data_pln = Xmr_Prices.query.filter_by(currency_id=19).first()
    xmr_data_pln.price = xmr_price_pln
    db.session.add(xmr_data_pln)

    # GBP
    xmr_price_gbp = (jsonprices['monero']['gbp'])
    xmr_data_gbp = Xmr_Prices.query.filter_by(currency_id=20).first()
    xmr_data_gbp.price = xmr_price_gbp
    db.session.add(xmr_data_gbp)

    # TRY
    xmr_price_try = (jsonprices['monero']['try'])
    xmr_data_try = Xmr_Prices.query.filter_by(currency_id=21).first()
    xmr_data_try.price = xmr_price_try
    db.session.add(xmr_data_try)

    # KRW
    xmr_price_krw = (jsonprices['monero']['krw'])
    xmr_data_krw = Xmr_Prices.query.filter_by(currency_id=22).first()
    xmr_data_krw.price = xmr_price_krw
    db.session.add(xmr_data_krw)

    # IDR
    xmr_price_idr = (jsonprices['monero']['idr'])
    xmr_data_idr = Xmr_Prices.query.filter_by(currency_id=23).first()
    xmr_data_idr.price = xmr_price_idr
    db.session.add(xmr_data_idr)

    # NZD
    xmr_price_nzd = (jsonprices['monero']['nzd'])
    xmr_data_nzd = Xmr_Prices.query.filter_by(currency_id=24).first()
    xmr_data_nzd.price = xmr_price_nzd
    db.session.add(xmr_data_nzd)

    # MYR
    xmr_price_myr = (jsonprices['monero']['myr'])
    xmr_data_myr = Xmr_Prices.query.filter_by(currency_id=25).first()
    xmr_data_myr.price = xmr_price_myr
    db.session.add(xmr_data_myr)

    # EUR
    xmr_price_eur = (jsonprices['monero']['eur'])
    xmr_data_eur = Xmr_Prices.query.filter_by(currency_id=26).first()
    xmr_data_eur.price = xmr_price_eur
    db.session.add(xmr_data_eur)

    # CZK
    xmr_price_czk = (jsonprices['monero']['czk'])
    xmr_data_czk = Xmr_Prices.query.filter_by(currency_id=27).first()
    xmr_data_czk.price = xmr_price_czk
    db.session.add(xmr_data_czk)
    