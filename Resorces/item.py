from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from Database.db import DB

db = DB()


class Item(Resource):
    @classmethod
    def find_by_name(cls, name):
        select_qry = f"SELECT * FROM items WHERE product_name='{name}'"
        selected_item = db.Execute(select_qry)

        return selected_item

    @jwt_required()
    def post(self):
        # use of request parser to validate the request body
        parser = reqparse.RequestParser()
        parser.add_argument('product_price', type=float, required=True, help="Product Price couldn't be blank")
        parser.add_argument('product_name', type=str, required=True, help="Product Name couldn't be blank")
        data = parser.parse_args()

        price = float(data['product_price'])
        name = str(data['product_name'])

        is_exist = self.find_by_name(name)

        if len(is_exist) > 0:
            return {"message": "Product Already Exist!"}, 409

        insert_qry = f"INSERT INTO items VALUES (NULL, '{name}', {price})"
        db.ExecuteNonQuery(insert_qry)

        return {"message": "Inserted Successfully!"}, 201

    @jwt_required()
    def put(self, name):
        """
        parser = reqparse.RequestParser()
        parser.add_argument('product_price', type=float, required=True, help="This field couldn't be blank")
        request_data = parser.parse_args()
        """
        # use request to get request body
        request_data = request.get_json()

        is_exist = self.find_by_name(name)

        if len(is_exist) > 0:
            update_query = f"UPDATE items SET price = {float(request_data['product_price'])} WHERE product_name='{name}'"
            print(update_query)
            db.ExecuteNonQuery(update_query)
            return {"message": "Product Updated Successfully!"}, 200
        return {"message": "No Data Found!"}, 404

    @jwt_required()
    def get(self, name):
        # use params from the end point
        selected_item = self.find_by_name(name)

        if len(selected_item) > 0:
            return {"item": {"name": selected_item[0][1], "price": selected_item[0][2]}}, 200
        return {"message": "No Item Found!"}, 404

    @jwt_required()
    def delete(self):
        # use query params
        data = request.args
        name = str(data['name'])

        selected_product = self.find_by_name(name)

        if len(selected_product) > 0:
            delete_query = f"DELETE FROM items WHERE product_name='{name}'"
            print(delete_query)
            db.ExecuteNonQuery(delete_query)
            return {"message": "Product Removed!"}, 200
        return {"message": "No Product Found!"}, 404


class Items(Resource):

    @jwt_required()
    def get(self):
        select_qry = f"SELECT * FROM items"
        all_items = db.Execute(select_qry)
        all_items = [{item[1]: item[2]} for item in all_items]

        if all_items is not None:
            return {"items": all_items}, 200
        else:
            return {"message": "Sorry, No Items Found!"}, 404