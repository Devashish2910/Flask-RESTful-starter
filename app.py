from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authentication, identity
from user import UserRegister
from item import Item, Items


app = Flask(__name__)
app.secret_key = "Devashish29101993"
api = Api(app)

jwt = JWT(app, authentication, identity)    # /auth


api.add_resource(Item, '/item', '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegister, '/sign_up', '/all_users')


if __name__ == '__main__':
    app.run(port=3000, debug=True)
