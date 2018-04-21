import os

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT
from datetime import timedelta

from Security.security import authentication, identity as identity_function
from Resorces.user import UserRegister
from Resorces.item import Item, Items
from Resorces.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///Database/data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = "Devashish29101993"
# default url for authentication is /auth, to change it
app.config['JWT_AUTH_URL_RULE'] = '/login'


jwt = JWT(app, authentication, identity_function)

@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    return jsonify({
                        'access_token': access_token.decode('utf-8'),
                        'user_id': identity.id
                   })

# config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

api = Api(app)

"""
@app.before_first_request
def create_tables():
    db.create_all()
"""


api.add_resource(Item, '/item', '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/signup', '/user')
api.add_resource(Store, '/store', '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    from Database.db import db

    db.init_app(app)
    app.run(port=3000, debug=True)
