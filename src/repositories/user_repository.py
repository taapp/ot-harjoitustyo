from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def insert_user(self, user):
        cur = self._connection.cursor()
        sql = """INSERT INTO users(id, name, password, is_admin) VALUES (?,?,?,?)"""
        cur.execute(sql, [user.id, user.name, user.password, int(user.admin)])
        self._connection.commit()

user_repository = UserRepository(get_database_connection())
