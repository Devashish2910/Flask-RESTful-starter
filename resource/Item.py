from flask import request
from flask_restful import Resource
from app import items

class Item(Resource):
    def post(self):
        request_data = request.get_json()
        if next(filter(lambda x: x['name'] == request_data['product_name'], items), None):
            return {"error": "Item already exist!"}, 400

        product = {
            'name': request_data['product_name'],
            'price': request_data['product_price']
        }
        items.append(product)
        return product, 201

    def put(self):
        request_data = request.get_json()

        for item in items:
            if item['name'] == request_data['product_name']:
                item['price'] = request_data['product_price']
                return item, 201
        return {"error:": "No Item Found!"}, 404

    def get(self, name):
        item = list(filter(lambda x: x['name'] == name, items))

        if len(item) > 0:
            return item[0], 200

        return {"error:": "No Item Found!"}, 404