from Database.db import db


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(100))
    items = db.relationship('ItemModel', lazy="dynamic")
    def __init__(self, name):
        self.store_name = name

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(store_name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def json(self):
        return {"store_id": self.id, "store_name": self.store_name, "items": [item.json() for item in self.items.all()]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()