from db import DB

db = DB()

class User:
    def __init__(self,  _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):

        qry = f"SELECT * FROM users WHERE username={username}"
        user_list = db.Execute(qry)

        if len(user_list) > 0:
            user = cls(user_list[0][0], user_list[0][1], user_list[0][2])
        else:
            user = None

        return user

    @classmethod
    def find_by_id(cls, id):

        qry = f"SELECT * FROM users WHERE username={id}"
        user_list = db.Execute(qry)

        if len(user_list) > 0:
            user = cls(user_list[0][0], user_list[0][1], user_list[0][2])
        else:
            user = None

        return user

