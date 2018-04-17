from Database.db import DB
from flask_restful import Resource
from flask import request

db = DB()


class User:

    def __init__(self,  _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):

        qry = f"SELECT * FROM users WHERE username='{username}'"
        user_list = db.Execute(qry)

        if len(user_list) > 0:
            user = cls(user_list[0][0], user_list[0][1], user_list[0][2])
        else:
            user = None

        return user

    @classmethod
    def find_by_id(cls, _id):

        qry = f"SELECT * FROM users WHERE id={int(_id)}"
        user_list = db.Execute(qry)

        if len(user_list) > 0:
            user = cls(user_list[0][0], user_list[0][1], user_list[0][2])
        else:
            user = None
        return user


class UserRegister(Resource):

    @staticmethod
    def post():
        """
        Method for Creating a new User
        :return: new created user notification
        :rtype: dictionary
        """
        data = request.get_json()

        _username = data['username']
        _password = data['password']

        check_exist = User.find_by_username(_username)

        if check_exist != None:
            return {"error:": "User Already Exist!"}, 409
        else:
            insert_qry = f"INSERT INTO users VALUES (NULL, '{_username}', '{_password}')"
            db.ExecuteNonQuery(insert_qry)
            return {"message:": "User Inserted Successfully!"}, 201

    @staticmethod
    def get():
        select_qry = f"SELECT * FROM users"
        result = db.Execute(select_qry)
        return {"users:": result}, 200


