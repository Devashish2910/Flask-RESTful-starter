from flask_restful import Resource,reqparse
from Models.store import StoreModel
from flask import request
from flask_jwt import jwt_required

class Store(Resource):

    @jwt_required()
    def post(self):
        """
        Create a new Store
        POST /store
        """
        parser = reqparse.RequestParser()
        parser.add_argument('store_name', type=str, required=True, help="Store Name couldn't be blank")
        data = parser.parse_args()

        name = data['store_name']

        exist = StoreModel.find_by_name(name)

        if exist:
            return {"message": "Store already exist!"}, 409

        store = StoreModel(name)
        store.save_to_db()

        return store.json(), 201

    @jwt_required()
    def get(self, name):
        """
        Find a store by name
        GET /store/<string:name>
        """
        exist = StoreModel.find_by_name(name)

        if not exist:
            return {"message": "Sorry, No Store Found!"}, 404
        else:
            return exist.json(), 200

    @jwt_required()
    def delete(self):
        """
        Delete a store
        DELETE /store?store_name=<string:name>
        """
        data = request.args
        store_name = data['store_name']

        exist = StoreModel.find_by_name(store_name)

        if exist:
            exist.delete()
            return {"message": "Item Removed!"}, 200

        return {"message", "Store don't exist!"}, 404

class StoreList(Resource):

    def get(self):
        """
        Get all Store details
        GET /stores
        """
        stores = StoreModel.find_all()

        if stores:
            return {"stores": [store.json() for store in stores]}, 200
        else:
            return {"message": "Sorry, No Store Found!"}, 404