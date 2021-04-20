from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def insert_user(self, user):
        cursor = self._connection.cursor()
        sql = """INSERT INTO users(id, name, password, is_admin) VALUES (?,?,?,?)"""
        cursor.execute(sql, [user.id, user.name, user.password, int(user.admin)])
        self._connection.commit()

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from users")
        self._connection.commit()

    def count_users(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")
        cnt = cursor.fetchone()
        return cnt


user_repository = UserRepository(get_database_connection())
