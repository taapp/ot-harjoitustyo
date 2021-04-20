import unittest

from services.question_service import question_service
from entities.answer import Answer


class TestQuestionService(unittest.TestCase):
    def setUp(self):
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
