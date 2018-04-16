from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authentication, identity

#from resource.Item import Item
#from resource.Items import Items


app = Flask(__name__)
app.secret_key = "Devashish29101993"
api = Api(app)

jwt = JWT(app, authentication, identity)    # /auth

items = []


class Item(Resource):
    @jwt_required()
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

    @jwt_required()
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('product_price', type=float, required=True, help="This field couldn't be blank")
        request_data = parser.parse_args()

        for item in items:
            if item['name'] == name:
                item['price'] = request_data['product_price']
                return item, 201
        return {"error:": "No Item Found!"}, 404

    @jwt_required()
    def get(self, name):
        item = list(filter(lambda x: x['name'] == name, items))

        if len(item) > 0:
            return item[0], 200
        return {"error:": "No Item Found!"}, 404

    @jwt_required()
    def delete(self):
        request_data = request.get_json()

        global items
        items = list(filter(lambda x: x['name'] != request_data['product_name'], items))
        return {"message:": "Item Deleted Successfully"}


class Items(Resource):

    @jwt_required()
    def get(self):
        return {"items": items}


api.add_resource(Item, '/item', '/item/<string:name>')
api.add_resource(Items, '/items')


if __name__ == '__main__':
    app.run(port=3000, debug=True)
