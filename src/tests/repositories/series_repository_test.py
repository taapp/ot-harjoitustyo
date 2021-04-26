import unittest

from repositories.series_repository import series_repository
from entities.question import Question
from entities.series import Series


class TestSeriesRepository(unittest.TestCase):
    def setUp(self):
        series_repository.delete_all()
        self.question_first = Question(
            "1508f410-6902-48d5-827d-d5a23f01cdf0", 1, "This is true", "Should be true")
        self.series_first = Series(
            "1508f410-6902-48d5-827d-d5a23f01asd1", "test_series")

    def test_insert_question(self):
        series_repository.insert_question(self.question_first)
        cnt = series_repository.count_questions()[0]
        self.assertEqual(cnt, 1)

    def test_insert_series(self):
        series_repository.insert_series(self.series_first)
        cnt = series_repository.count_series()[0]
        self.assertEqual(cnt, 1)

    def test_insert_series_questions(self):
        series_repository.insert_series_questions(
            self.series_first.id, self.question_first.id)
        cnt = series_repository.count_series_questions()[0]
        self.assertEqual(cnt, 1)
