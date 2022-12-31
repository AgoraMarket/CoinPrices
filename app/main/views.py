from flask import jsonify
from app.scripts import\
    bch_price,\
    btc_price,\
    xmr_price

from app import app, db
from pycoingecko import CoinGeckoAPI
from app.classes.wallet_btc import Btc_Prices
from app.classes.wallet_bch import Bch_Prices
from app.classes.wallet_xmr import Xmr_Prices


@app.route('/', methods=['GET'])
def get_daemon_status():
    """
    Gets the count of vendor order issues.  Notification bar at top
    :return:
    """

    return jsonify({
        "status": 'Ready to get coin prices',
    })

@app.route('/price', methods=['GET'])
def priceofit():
    """
    Gets the price of xmr in 5 diff currencies
    :return:
    """
    
    cg = CoinGeckoAPI()
    print("hello")
    get_price_json = cg.get_price(ids='bitcoin, bitcoin-cash, monero', vs_currencies='usd,\
                                  php, chf, cad, thb, dkk,sek,sgd,nok,brl,ils,inr,zar,\
                                  hkd,jpy,huf,mxn,cny,aud,pln,gbp,try,krw,idr,nzd,myr,eur,czk')
    
    
    bch_price.get_prices_coins_bch(jsonprices=get_price_json)
    btc_price.get_prices_coins_btc(jsonprices=get_price_json)
    xmr_price.get_prices_coins_xmr(jsonprices=get_price_json)
    
    

    db.session.commit()
    return jsonify("success")


@app.route('/xmr', methods=['GET'])
def get_xmr_price():
    """
    Gets the price of xmr in 5 diff currencies
    :return:
    """
    cg = CoinGeckoAPI()

    get_price_json = cg.get_price(ids='bitcoin, bitcoin-cash, monero',
                                  vs_currencies='usd, php, chf, cad, \
                                  thb, dkk,sek,sgd,nok,brl,ils,inr,zar,hkd,\
                                  jpy,huf,mxn,cny,aud,pln,gbp,try,\
                                  krw,idr,nzd,myr,eur,czk')
    try:
        
        xmr_price.get_prices_coins_xmr(jsonprices=get_price_json)
        
        return jsonify({
            "status": 'Updated XMR Prices',
        })
        
    except Exception as e:
        return jsonify({
            "status": str(e),
        })


@app.route('/btc', methods=['GET'])
def get_btc_price():
    """
    Gets the price of btc in 5 diff currencies
    :return:
    """
    cg = CoinGeckoAPI()

    get_price_json = cg.get_price(ids='bitcoin, bitcoin-cash, monero',
                                  vs_currencies='usd, php, chf, cad,\
                                  thb, dkk,sek,sgd,nok,brl,ils,inr,zar,\
                                  hkd,jpy,huf,mxn,cny,aud,pln,gbp,try,krw,\
                                  idr,nzd,myr,eur,czk')
    try:
        
        btc_price.get_prices_coins_btc(jsonprices=get_price_json)
        
        return jsonify({
            "status": 'Updated BTC Prices',
        })
        
    except Exception as e:
        return jsonify({
            "status": 'Failed to update BTC Prices',
        })


@app.route('/bch', methods=['GET'])
def get_bch_price():
    """
    Gets the price of bch in 5 diff currencies
    :return:
    """
    cg = CoinGeckoAPI()

    get_price_json = cg.get_price(ids='bitcoin, bitcoin-cash, monero',
                                  vs_currencies='usd, php, chf, cad, thb, \
                                  dkk,sek,sgd,nok,brl,ils,inr,zar,hkd,\
                                  jpy,huf,mxn,cny,aud,pln,gbp,try,krw,\
                                  idr,nzd,myr,eur,czk')
    try:
        
        bch_price.get_prices_coins_bch(jsonprices=get_price_json)
        
        return jsonify({
            "status": 'Updated BCH Prices',
        })
        
    except Exception as e:
        return jsonify({
            "status": 'Failed to update BCH Prices',
        })
