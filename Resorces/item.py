from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from Models.item import ItemModel


class Item(Resource):
    @jwt_required()
    def post(self):
        # use of request parser to validate the request body
        parser = reqparse.RequestParser()
        parser.add_argument('product_price', type=float, required=True, help="Product Price couldn't be blank")
        parser.add_argument('product_name', type=str, required=True, help="Product Name couldn't be blank")
        data = parser.parse_args()

        price = data['product_price']
        name = data['product_name']

        exist = ItemModel.find_by_name(name)

        if exist:
            return {"message": "Product Already Exist!"}, 409

        item = ItemModel(name, price)
        item.save_to_db()
        return item.json(), 201

    @jwt_required()
    def put(self, name):
        """
        parser = reqparse.RequestParser()
        parser.add_argument('product_price', type=float, required=True, help="This field couldn't be blank")
        request_data = parser.parse_args()
        """
        # use request to get request body
        request_data = request.get_json()

        item = ItemModel.find_by_name(name)

        if item:
            item.product_price = float(request_data['product_price'])
            item.save_to_db()
            return item.json(), 201
        return {"message": "No Data Found!"}, 404

    @jwt_required()
    def get(self, name):
        # use params from the end point
        selected_item = ItemModel.find_by_name(name)

        if selected_item:
            return selected_item.json(), 200
        return {"message": "No Item Found!"}, 404

    @jwt_required()
    def delete(self):
        # use query params
        data = request.args
        name = str(data['name'])

        selected_product = ItemModel.find_by_name(name)

        if selected_product:
            selected_product.delete()
            return {"message": "Product Removed!"}, 200
        return {"message": "No Product Found!"}, 404


class Items(Resource):

    @jwt_required()
    def get(self):
        items = ItemModel.find_all()

        if items:
            #return {"users": [item.json() for item in items]}, 200
            return {"users": list(map(lambda x: x.json(), items))}
        else:
            return {"message": "Sorry, No Items Found!"}, 404