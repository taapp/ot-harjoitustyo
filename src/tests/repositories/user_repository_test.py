import unittest

from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_first = User(
            "f2158b81-3374-4f2d-9831-fc5667aae1fd", "first", "passwd", False)

    def test_insert_user(self):
        user_repository.insert_user(self.user_first)
        cnt = user_repository.count_users()[0]
        self.assertEqual(cnt, 1)

    def test_exists_username(self):
        user_repository.insert_user(self.user_first)
        res_first = user_repository.exists_username('first')
        res_second = user_repository.exists_username('second')
        self.assertEqual(res_first, True)
        self.assertEqual(res_second, False)

    def test_load_user(self):
        user_repository.insert_user(self.user_first)
        res_first = user_repository.load_user('first', 'passwd')
        res_wrong_password = user_repository.load_user('first', 'passwd1')
        self.assertEqual(res_first.password, "passwd")
        self.assertEqual(res_wrong_password, None)
