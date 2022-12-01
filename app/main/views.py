from flask import jsonify
from app.scripts import\
    bch_price,\
    btc_price,\
    xmr_price
from app import app


@app.route('/status', methods=['GET'])
def get_daemon_status():
    """
    Gets the count of vendor order issues.  Notification bar at top
    :return:
    """

    return jsonify({
        "status": 'Ready to get coin prices',
    })


@app.route('/xmr', methods=['GET'])
def get_xmr_price():
    """
    Gets the price of xmr in 5 diff currencies
    :return:
    """
    try:
        
        xmr_price()
        
        return jsonify({
            "status": 'Updated XMR Prices',
        })
        
    except:
        
        return jsonify({
            "status": 'Failed to update XMR Prices',
        })


@app.route('/btc', methods=['GET'])
def get_btc_price():
    """
    Gets the price of btc in 5 diff currencies
    :return:
    """
    try:
        
        btc_price()
        
        return jsonify({
            "status": 'Updated BTC Prices',
        })
        
    except:
        
        return jsonify({
            "status": 'Failed to update BTC Prices',
        })


@app.route('/bch', methods=['GET'])
def get_bch_price():
    """
    Gets the price of bch in 5 diff currencies
    :return:
    """
    try:
        
        bch_price()
        
        return jsonify({
            "status": 'Updated BCH Prices',
        })
        
    except:
        
        return jsonify({
            "status": 'Failed to update BCH Prices',
        })
