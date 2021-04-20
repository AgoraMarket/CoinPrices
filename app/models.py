from app import db


class btc_cash_Prices(db.Model):
    __tablename__ = 'prices_btc_cash'
    __bind_key__ = 'agora'
    __table_args__ = {"schema": "public", 'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    currency = db.Column(db.TEXT)
    price = db.Column(db.DECIMAL(50, 2))
    currency_id = db.Column(db.INTEGER)
    percent_change_twentyfour = db.Column(db.DECIMAL(50, 2))
