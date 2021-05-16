from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    """Luokka, joka vastaa käyttäjätiedon tallentamisesta ja hakemisesta tietokannasta.
    """

    def __init__(self, connection):
        self._connection = connection

    def insert_user(self, user):
        """Lisää uuden käyttäjän käyttäjätauluun

        Args:
            user: User-olio, joka vastaa käyttäjää, jonka tiedot lisätään tietokantaan.
        """

        cursor = self._connection.cursor()
        sql = """INSERT INTO users(id, name, password, is_admin) VALUES (?,?,?,?)"""
        cursor.execute(
            sql, [user.id, user.name, user.password, int(user.admin)])
        self._connection.commit()

    def delete_all(self):
        """Poistaa tiedot käyttäjätaulusta.
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from users")
        self._connection.commit()

    def count_users(self):
        """Laskee tallennettujen käyttäjien määrän.

        Returns:
            cnt: Kokonaisluku, joka vastaa tallennettujen käyttäjien määrää
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")
        cnt = cursor.fetchone()
        return cnt

    def load_user(self, username, password):
        cursor = self._connection.cursor()
        cursor.execute("SELECT id,name,password,is_admin FROM users WHERE name=? AND password=?", [
                       username, password])
        res = cursor.fetchone()
        if res is not None:
            user = User(res[0], res[1], res[2], res[3])
            return user
        return None

    def exists_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE name=?", [username])
        cnt = cursor.fetchone()[0]
        if cnt >= 1:
            return True
        return False


user_repository = UserRepository(get_database_connection())
