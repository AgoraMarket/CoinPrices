from flask import jsonify
from app.scripts import\
    bch_price,\
    btc_price,\
    xmr_price

from app import app, db
from pycoingecko import CoinGeckoAPI



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
    Gets the price of xmr,bch,btc in all currencies
    :return:
    """
    
    cg = CoinGeckoAPI()

    get_price_json = cg.get_price(ids='bitcoin, bitcoin-cash, monero', vs_currencies='usd,\
                                  php, chf, cad, thb, dkk,sek,sgd,nok,brl,ils,inr,zar,\
                                  hkd,jpy,huf,mxn,cny,aud,pln,gbp,try,krw,idr,nzd,myr,eur,czk')
    
    
    bch_price.get_prices_coins_bch(jsonprices=get_price_json)
    btc_price.get_prices_coins_btc(jsonprices=get_price_json)
    xmr_price.get_prices_coins_xmr(jsonprices=get_price_json)
    
    db.session.commit()
    return jsonify("success")

