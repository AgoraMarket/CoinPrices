from app import db


class BchPrices(db.Model):
    __tablename__ = 'prices_bch'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_main"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL(50, 2))

db.create_all()
db.session.commit()