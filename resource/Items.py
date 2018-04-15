from flask_restful import Resource
from app import items


class Items(Resource):
    def get(self):
        return {"items": items}