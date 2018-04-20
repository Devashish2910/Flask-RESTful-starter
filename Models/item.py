from Database.db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    product_price = db.Column(db.Float(precision=2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.product_name = name
        self.product_price = price
        self.store_id = store_id

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(product_name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def json(self):
        return {"name": self.product_name, "price": self.product_price}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        pass

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()