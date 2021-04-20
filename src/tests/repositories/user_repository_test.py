import unittest

from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_first = User("f2158b81-3374-4f2d-9831-fc5667aae1fd", "first", "passwd", False)

    def test_insert_user(self):
        user_repository.insert_user(self.user_first)
        cnt = user_repository.count_users()[0]
        self.assertEqual(cnt, 1)
