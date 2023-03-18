
from app import db
from app.classes.wallet_btc import Btc_Prices


def get_prices_coins_btc(jsonprices):
    """
    used pycoingecko modules for prices
    """

    # USD
    btc_price_usd = (jsonprices['bitcoin']['usd'])
    btc_data_usd = Btc_Prices.query.filter_by(currency_id=0).first()
    btc_data_usd.price = btc_price_usd
    db.session.add(btc_data_usd)
    print(btc_data_usd.price)
    # PHP
    btc_price_php = (jsonprices['bitcoin']['php'])
    btc_data_php = Btc_Prices.query.filter_by(currency_id=1).first()
    btc_data_php.price = btc_price_php
    db.session.add(btc_data_php)
    
    # CHF
    btc_price_chf = (jsonprices['bitcoin']['chf'])
    btc_data_chf = Btc_Prices.query.filter_by(currency_id=2).first()
    btc_data_chf.price = btc_price_chf
    db.session.add(btc_data_chf)
    
    # CAD
    btc_price_cad = (jsonprices['bitcoin']['cad'])
    btc_data_cad = Btc_Prices.query.filter_by(currency_id=3).first()
    btc_data_cad.price = btc_price_cad
    db.session.add(btc_data_cad)

    # SGD
    btc_price_sgd = (jsonprices['bitcoin']['sgd'])
    btc_data_sgd = Btc_Prices.query.filter_by(currency_id=4).first()
    btc_data_sgd.price = btc_price_sgd
    db.session.add(btc_data_sgd)
    
    # DKK
    btc_price_dkk = (jsonprices['bitcoin']['dkk'])
    btc_data_dkk = Btc_Prices.query.filter_by(currency_id=5).first()
    btc_data_dkk.price = btc_price_dkk
    db.session.add(btc_data_dkk)
    
    # NOK
    btc_price_nok = (jsonprices['bitcoin']['nok'])
    btc_data_nok = Btc_Prices.query.filter_by(currency_id=6).first()
    btc_data_nok.price = btc_price_nok
    db.session.add(btc_data_nok)
    
    # ILS
    btc_price_ils = (jsonprices['bitcoin']['ils'])
    btc_data_ils = Btc_Prices.query.filter_by(currency_id=7).first()
    btc_data_ils.price = btc_price_ils
    db.session.add(btc_data_ils)
    
    # SEK
    btc_price_sek = (jsonprices['bitcoin']['sek'])
    btc_data_sek = Btc_Prices.query.filter_by(currency_id=8).first()
    btc_data_sek.price = btc_price_sek
    db.session.add(btc_data_sek)

    # THB
    btc_price_thb = (jsonprices['bitcoin']['thb'])
    btc_data_thb = Btc_Prices.query.filter_by(currency_id=9).first()
    btc_data_thb.price = btc_price_thb
    db.session.add(btc_data_thb)
    
    # BRL
    btc_price_brl = (jsonprices['bitcoin']['brl'])
    btc_data_brl = Btc_Prices.query.filter_by(currency_id=10).first()
    btc_data_brl.price = btc_price_brl
    db.session.add(btc_data_brl)
    
    # INR
    btc_price_inr = (jsonprices['bitcoin']['inr'])
    btc_data_inr = Btc_Prices.query.filter_by(currency_id=11).first()
    btc_data_inr.price = btc_price_inr
    db.session.add(btc_data_inr)
    
    # ZAR
    btc_price_zar = (jsonprices['bitcoin']['zar'])
    btc_data_zar = Btc_Prices.query.filter_by(currency_id=12).first()
    btc_data_zar.price = btc_price_zar
    db.session.add(btc_data_zar)
        
    # HKD
    btc_price_hkd = (jsonprices['bitcoin']['hkd'])
    btc_data_hkd = Btc_Prices.query.filter_by(currency_id=13).first()
    btc_data_hkd.price = btc_price_hkd
    db.session.add(btc_data_hkd)
    
    # JPY
    btc_price_jpy = (jsonprices['bitcoin']['jpy'])
    btc_data_jpy = Btc_Prices.query.filter_by(currency_id=14).first()
    btc_data_jpy.price = btc_price_jpy
    db.session.add(btc_data_jpy)
    
    # HUF
    btc_price_huf = (jsonprices['bitcoin']['huf'])
    btc_data_huf = Btc_Prices.query.filter_by(currency_id=15).first()
    btc_data_huf.price = btc_price_huf
    db.session.add(btc_data_huf)
    
    # MXN
    btc_price_mxn = (jsonprices['bitcoin']['mxn'])
    btc_data_mxn = Btc_Prices.query.filter_by(currency_id=16).first()
    btc_data_mxn.price = btc_price_mxn
    db.session.add(btc_data_mxn)
    
    # CNY
    btc_price_cny = (jsonprices['bitcoin']['cny'])
    btc_data_cny = Btc_Prices.query.filter_by(currency_id=17).first()
    btc_data_cny.price = btc_price_cny
    db.session.add(btc_data_mxn)
    
    # AUD
    btc_price_aud = (jsonprices['bitcoin']['aud'])
    btc_data_aud = Btc_Prices.query.filter_by(currency_id=18).first()
    btc_data_aud.price = btc_price_aud
    db.session.add(btc_data_aud)
    
    # PLN
    btc_price_pln = (jsonprices['bitcoin']['pln'])
    btc_data_pln = Btc_Prices.query.filter_by(currency_id=19).first()
    btc_data_pln.price = btc_price_pln
    db.session.add(btc_data_pln)
    
    # GBP
    btc_price_gbp = (jsonprices['bitcoin']['gbp'])
    btc_data_gbp = Btc_Prices.query.filter_by(currency_id=20).first()
    btc_data_gbp.price = btc_price_gbp
    db.session.add(btc_data_gbp)
    
    # TRY
    btc_price_try = (jsonprices['bitcoin']['try'])
    btc_data_try = Btc_Prices.query.filter_by(currency_id=21).first()
    btc_data_try.price = btc_price_try
    db.session.add(btc_data_try)
    
    # KRW
    btc_price_krw = (jsonprices['bitcoin']['krw'])
    btc_data_krw = Btc_Prices.query.filter_by(currency_id=22).first()
    btc_data_krw.price = btc_price_krw
    db.session.add(btc_data_krw)
    
    # IDR
    btc_price_idr = (jsonprices['bitcoin']['idr'])
    btc_data_idr = Btc_Prices.query.filter_by(currency_id=23).first()
    btc_data_idr.price = btc_price_idr
    db.session.add(btc_data_idr)
    
    # NZD
    btc_price_nzd = (jsonprices['bitcoin']['nzd'])
    btc_data_nzd = Btc_Prices.query.filter_by(currency_id=24).first()
    btc_data_nzd.price = btc_price_nzd
    db.session.add(btc_data_nzd)

    # MYR
    btc_price_myr = (jsonprices['bitcoin']['myr'])
    btc_data_myr = Btc_Prices.query.filter_by(currency_id=25).first()
    btc_data_myr.price = btc_price_myr
    db.session.add(btc_data_myr)

    # EUR
    btc_price_eur = (jsonprices['bitcoin']['eur'])
    btc_data_eur = Btc_Prices.query.filter_by(currency_id=26).first()
    btc_data_eur.price = btc_price_eur
    db.session.add(btc_data_eur)
    
    # CZK
    btc_price_czk = (jsonprices['bitcoin']['czk'])
    btc_data_czk = Btc_Prices.query.filter_by(currency_id=27).first()
    btc_data_czk.price = btc_price_czk
    db.session.add(btc_data_czk)
