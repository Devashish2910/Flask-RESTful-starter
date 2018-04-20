from flask_restful import Resource, reqparse
from flask import request
from Models.user import UserModel


class UserRegister(Resource):
    @staticmethod
    def post():
        """
        Method for Creating a new User
        :return: new created user notification
        :rtype: dictionary
        """
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True, help="*username required")
        parser.add_argument('password', required=True, help="*password required")
        data = parser.parse_args()

        _username = data['username']
        _password = str(data['password'])

        check_exist = UserModel.find_by_username(_username)

        if check_exist:
            return {"error:": "User Already Exist!"}, 409
        else:
            new_user = UserModel(_username, _password)
            new_user.save_to_db()
            return new_user.json(), 201

    @staticmethod
    def get():
        data = request.args
        _username = str(data['username'])

        if _username == '$_give_me_all_users_$':
            all_users = UserModel.find_all()
            return {"user_details": [user.json() for user in all_users]}, 200
        else:
            user = UserModel.find_by_username(_username)

            if user is not None:
                return user.json(), 200
            else:
                return {"message": "No user Found"}, 404




