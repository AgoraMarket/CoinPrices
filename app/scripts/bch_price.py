
from app import db
from app.classes.wallet_bch import Bch_Prices


def get_prices_coins_bch(jsonprices):
    """
    used pycoingecko modules for prices
    """
    print(jsonprices)
    # USD
    bch_price_usd = (jsonprices['bitcoin']['usd'])
    bch_data_usd = Bch_Prices.query.filter_by(currency_id=0).first()
    bch_data_usd.price = bch_price_usd
    db.session.add(bch_data_usd)
    
    # PHP
    bch_price_php = (jsonprices['bitcoin']['php'])
    bch_data_php = Bch_Prices.query.filter_by(currency_id=1).first()
    bch_data_php.price = bch_price_php
    db.session.add(bch_data_php)
    
    # CHF
    bch_price_chf = (jsonprices['bitcoin']['chf'])
    bch_data_chf = Bch_Prices.query.filter_by(currency_id=2).first()
    bch_data_chf.price = bch_price_chf
    db.session.add(bch_data_chf)
    
    # CAD
    bch_price_cad = (jsonprices['bitcoin']['cad'])
    bch_data_cad = Bch_Prices.query.filter_by(currency_id=3).first()
    bch_data_cad.price = bch_price_cad
    db.session.add(bch_data_cad)
    
    # SGD
    bch_price_sgd = (jsonprices['bitcoin']['sgd'])
    bch_data_sgd = Bch_Prices.query.filter_by(currency_id=4).first()
    bch_data_sgd.price = bch_price_sgd
    db.session.add(bch_data_sgd)

    # DKK
    bch_price_dkk = (jsonprices['bitcoin']['dkk'])
    bch_data_dkk = Bch_Prices.query.filter_by(currency_id=5).first()
    bch_data_dkk.price = bch_price_dkk
    db.session.add(bch_data_dkk)
    
    # NOK
    bch_price_nok = (jsonprices['bitcoin']['nok'])
    bch_data_nok = Bch_Prices.query.filter_by(currency_id=6).first()
    bch_data_nok.price = bch_price_nok
    db.session.add(bch_data_nok)
    
    # ILS
    bch_price_ils = (jsonprices['bitcoin']['ils'])
    bch_data_ils = Bch_Prices.query.filter_by(currency_id=7).first()
    bch_data_ils.price = bch_price_ils
    db.session.add(bch_data_ils)

    # SEK
    bch_price_sek = (jsonprices['bitcoin']['sek'])
    bch_data_sek = Bch_Prices.query.filter_by(currency_id=8).first()
    bch_data_sek.price = bch_price_sek
    db.session.add(bch_data_sek)
    
    # THB
    bch_price_thb = (jsonprices['bitcoin']['thb'])
    bch_data_thb = Bch_Prices.query.filter_by(currency_id=9).first()
    bch_data_thb.price = bch_price_thb
    db.session.add(bch_data_thb)

    # BRL
    bch_price_brl = (jsonprices['bitcoin']['brl'])
    bch_data_brl = Bch_Prices.query.filter_by(currency_id=10).first()
    bch_data_brl.price = bch_price_brl
    db.session.add(bch_data_brl)
    
    # INR
    bch_price_inr = (jsonprices['bitcoin']['inr'])
    bch_data_inr = Bch_Prices.query.filter_by(currency_id=11).first()
    bch_data_inr.price = bch_price_inr
    db.session.add(bch_data_inr)
    
    # ZAR
    bch_price_zar = (jsonprices['bitcoin']['zar'])
    bch_data_zar = Bch_Prices.query.filter_by(currency_id=12).first()
    bch_data_zar.price = bch_price_zar
    db.session.add(bch_data_zar)
    
    # HKD
    bch_price_hkd = (jsonprices['bitcoin']['hkd'])
    bch_data_hkd = Bch_Prices.query.filter_by(currency_id=13).first()
    bch_data_hkd.price = bch_price_hkd
    db.session.add(bch_data_hkd)
    
    # JPY
    bch_price_jpy = (jsonprices['bitcoin']['jpy'])
    bch_data_jpy = Bch_Prices.query.filter_by(currency_id=14).first()
    bch_data_jpy.price = bch_price_jpy
    db.session.add(bch_data_jpy)
    
    # HUF
    bch_price_huf = (jsonprices['bitcoin']['huf'])
    bch_data_huf = Bch_Prices.query.filter_by(currency_id=15).first()
    bch_data_huf.price = bch_price_huf
    db.session.add(bch_data_huf)
    
    # MXN
    bch_price_mxn = (jsonprices['bitcoin']['mxn'])
    bch_data_mxn = Bch_Prices.query.filter_by(currency_id=16).first()
    bch_data_mxn.price = bch_price_mxn
    db.session.add(bch_data_mxn)
    
    # CNY
    bch_price_cny = (jsonprices['bitcoin']['cny'])
    bch_data_cny = Bch_Prices.query.filter_by(currency_id=17).first()
    bch_data_cny.price = bch_price_cny
    db.session.add(bch_data_mxn)
    
    # AUD
    bch_price_aud = (jsonprices['bitcoin']['aud'])
    bch_data_aud = Bch_Prices.query.filter_by(currency_id=18).first()
    bch_data_aud.price = bch_price_aud
    db.session.add(bch_data_aud)
    
    # PLN
    bch_price_pln = (jsonprices['bitcoin']['pln'])
    bch_data_pln = Bch_Prices.query.filter_by(currency_id=19).first()
    bch_data_pln.price = bch_price_pln
    db.session.add(bch_data_pln)
    
    # GBP
    bch_price_gbp = (jsonprices['bitcoin']['gbp'])
    bch_data_gbp = Bch_Prices.query.filter_by(currency_id=20).first()
    bch_data_gbp.price = bch_price_gbp
    db.session.add(bch_data_gbp)
    
    # TRY
    bch_price_try = (jsonprices['bitcoin']['try'])
    bch_data_try = Bch_Prices.query.filter_by(currency_id=21).first()
    bch_data_try.price = bch_price_try
    db.session.add(bch_data_try)
    
    # KRW
    bch_price_krw = (jsonprices['bitcoin']['krw'])
    bch_data_krw = Bch_Prices.query.filter_by(currency_id=22).first()
    bch_data_krw.price = bch_price_krw
    db.session.add(bch_data_krw)
    
    # IDR
    bch_price_idr = (jsonprices['bitcoin']['idr'])
    bch_data_idr = Bch_Prices.query.filter_by(currency_id=23).first()
    bch_data_idr.price = bch_price_idr
    db.session.add(bch_data_idr)
    
    # NZD
    bch_price_nzd = (jsonprices['bitcoin']['nzd'])
    bch_data_nzd = Bch_Prices.query.filter_by(currency_id=24).first()
    bch_data_nzd.price = bch_price_nzd
    db.session.add(bch_data_nzd)

    # MYR
    bch_price_myr = (jsonprices['bitcoin']['myr'])
    bch_data_myr = Bch_Prices.query.filter_by(currency_id=25).first()
    bch_data_myr.price = bch_price_myr
    db.session.add(bch_data_myr)

    # EUR
    bch_price_eur = (jsonprices['bitcoin']['eur'])
    bch_data_eur = Bch_Prices.query.filter_by(currency_id=26).first()
    bch_data_eur.price = bch_price_eur
    db.session.add(bch_data_eur)
    
    # CZK
    bch_price_czk = (jsonprices['bitcoin']['czk'])
    bch_data_czk = Bch_Prices.query.filter_by(currency_id=27).first()
    bch_data_czk.price = bch_price_czk
    db.session.add(bch_data_czk)
    