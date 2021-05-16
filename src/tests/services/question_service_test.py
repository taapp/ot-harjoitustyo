import unittest

from services.question_service import question_service
from entities.answer import Answer
from build import build


class TestQuestionService(unittest.TestCase):
    def setUp(self):
        build()
        question_service.load_default_series()
        question_service.cur_answers.append(
            Answer(1, question_service.cur_series.questions[0], 1))
        question_service.cur_answers.append(
            Answer(2, question_service.cur_series.questions[1], 0.5))
        question_service.cur_answers.append(
            Answer(3, question_service.cur_series.questions[2], 0))

    def test_get_total_score(self):
        total_score = question_service.get_total_score()
        self.assertEqual(total_score, 0.5**2/3)

    def test_create_user(self):
        user = question_service.create_user('Kalle', 'passu', False)
        self.assertEqual(user.__str__(), "User, name: Kalle, type: False")

    def test_load_series_by_name(self):
        question_service.load_series_by_name("default")
        self.assertEqual(question_service.cur_series.name, "default")

    def test_load_all_questions(self):
        question_service.load_all_questions()
        self.assertEqual(len(question_service.list_questions), 3)

    def test_load_user(self):
        user_unknown = question_service.load_user('tuntematon', 'passut')
        self.assertEqual(user_unknown, None)

    def test_save_user(self):
        res = question_service.save_user('Kalle', 'passu', False)
        self.assertEqual(res, True)
        res_2 = question_service.save_user('Kalle', 'passu', False)
        self.assertEqual(res_2, False)

    def test_set_current_user(self):
        user = question_service.create_user('Kalle', 'passu', False)
        question_service.set_current_user(user)
        self.assertEqual(question_service.cur_user.password, "passu")

    def test_current_user_is_admin(self):
        res_no_user = question_service.current_user_is_admin()
        self.assertEqual(res_no_user, None)
        user = question_service.create_user('Kalle', 'passu', False)
        question_service.set_current_user(user)
        res_not_admin = question_service.current_user_is_admin()
        self.assertEqual(res_not_admin, False)
        user_admin = question_service.create_user('Ville', 'salsasana', True)
        question_service.set_current_user(user_admin)
        res_admin = question_service.current_user_is_admin()
        self.assertEqual(res_admin, True)

    def test_create_uuid(self):
        uuid_new = question_service.create_uuid()
        self.assertEqual(len(uuid_new), 36)
        self.assertEqual(type(uuid_new), str)
