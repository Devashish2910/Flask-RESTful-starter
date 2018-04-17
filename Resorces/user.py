from Database.db import DB
from flask_restful import Resource, reqparse
from flask import request
from Models.user import UserModel

db = DB()


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

        if check_exist != None:
            return {"error:": "User Already Exist!"}, 409
        else:
            insert_qry = f"INSERT INTO users VALUES (NULL, '{_username}', '{_password}')"
            db.ExecuteNonQuery(insert_qry)
            return {"message:": "User Inserted Successfully!"}, 201

    @staticmethod
    def get():
        data = request.args
        _username = str(data['username'])

        if _username == '$_give_me_all_users_$':
            select_qry = f"SELECT * FROM users"
            result = db.Execute(select_qry)
            return {"user_details": result}, 200
        else:
            qry = f"SELECT * FROM users WHERE username='{_username}'"
            user_list = db.Execute(qry)

            if user_list is not None:
                return {"user_details": {"username": user_list[0][1], "password": user_list[0][2]}}, 200
            else:
                return {"message": "No user Found"}, 404




