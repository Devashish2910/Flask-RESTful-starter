from Database.db import DB
db = DB()


class ItemModel:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def find_by_name(cls, name):
        select_qry = f"SELECT * FROM items WHERE product_name='{name}'"
        selected_item = db.Execute(select_qry)

        return selected_item
