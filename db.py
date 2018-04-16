import sqlite3

database_path = "data.db"

class DB:
    def __init__(self):
        """
        Initialize database and tables
        """
        conn = sqlite3.connect(database_path)
        cur = conn.cursor()
        users = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)"
        tables = [users]
        try:
            for table in tables:
                cur.execute(table)
            conn.commit()
        except Exception as ex:
            print(ex.args)
        finally:
            conn.close()

    @staticmethod
    def ExecuteNonQuery(qry):
        """
        Method for Update, Insert, Delete Query
        :param qry: Query String
        :type qry: string
        :return: Nothing
        :rtype: None
        """
        conn = sqlite3.connect(database_path)
        cur = conn.cursor()
        try:
            cur.execute(qry)
            conn.commit()
        except Exception as ex:
            return ex.args
        finally:
            conn.close()

    @staticmethod
    def Execute(qry):
        """
        Method for Select Query
        :param qry: Query String
        :type qry: string
        :return: List of results
        :rtype: list
        """
        conn = sqlite3.connect(database_path)
        cur = conn.cursor()
        try:
            cur.execute(qry)
            res = cur.fetchall()
            return res
        except Exception as ex:
            return ex.args
        finally:
            conn.close()

