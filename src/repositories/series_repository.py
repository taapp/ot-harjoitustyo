from pathlib import Path
import csv
import uuid
from entities.question import Question
from entities.series import Series
from database_connection import get_database_connection

NAME_SERIES_DEFAULT = 'default'


class SeriesRepository:

    def __init__(self, file_path, connection):
        self.file_path = file_path
        self._connection = connection

    def read_default_series_file(self):
        series = Series(self.create_uuid(), NAME_SERIES_DEFAULT)
        questions = []
        with open(self.file_path) as file:
            reader = csv.reader(file, delimiter=",")
            for i, row in enumerate(reader):
                if i != 0:
                    questions.append(
                        # Question(int(row[0]), int(row[1]), row[2], row[3]))
                        Question(self.create_uuid(), int(row[1]), row[2], row[3]))
        series.set_all_questions(questions)
        return series

    def get_default_series(self):
        series = self.get_series_by_name(NAME_SERIES_DEFAULT)
        series = self.get_questions_for_series(series)
        return series

    def get_series(self, id_series):
        series = self.get_series_by_id(id_series)
        series = self.get_questions_for_series(series)
        return series

    def create_uuid(self):
        uuid_new = str(uuid.uuid4())
        return uuid_new

    def insert_question(self, question):
        cursor = self._connection.cursor()
        sql = """INSERT INTO questions(id, truth, statement, comment) VALUES (?,?,?,?)"""
        cursor.execute(
            sql, [question.id, int(question.truth), question.statement, question.comment])
        self._connection.commit()

    def delete_all_questions(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from questions")
        self._connection.commit()

    def count_table(self, table_name):
        cursor = self._connection.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        cnt = cursor.fetchone()
        return cnt

    def count_questions(self):
        return self.count_table('questions')

    def count_series(self):
        return self.count_table('series')

    def count_series_questions(self):
        return self.count_table('series_questions')

    def insert_series(self, series):
        cursor = self._connection.cursor()
        sql = """INSERT INTO series(id, name) VALUES (?,?)"""
        cursor.execute(
            sql, [series.id, series.name])
        self._connection.commit()

    def get_series_by_name(self, name):
        cursor = self._connection.cursor()
        cursor.execute("SELECT id, name FROM series WHERE name=?", [name])
        id_series, name = cursor.fetchone()
        return Series(id_series, name)

    def get_series_by_id(self, id_series):
        cursor = self._connection.cursor()
        cursor.execute("SELECT id, name FROM series WHERE id=?", [id_series])
        id_series, name = cursor.fetchone()
        return Series(id_series, name)

    def get_series_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT id, name FROM series")
        fetched = cursor.fetchall()
        ls_series = [Series(*t) for t in fetched]
        return ls_series

    def get_questions_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT id, truth, statement, comment FROM questions")
        fetched = cursor.fetchall()
        ls_questions = [Question(*t) for t in fetched]
        return ls_questions

    def get_questions_for_series(self, series):
        series.empty_questions()
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT id_question FROM series_questions WHERE id_series=?", [series.id])
        ids_questions = cursor.fetchall()
        if ids_questions is None:
            return None
        for id_question in ids_questions:
            cursor.execute(
                "SELECT id, truth, statement, comment FROM questions WHERE id=?", id_question)
            id_question, truth, statement, comment = cursor.fetchone()
            question = Question(
                id_question, truth, statement, comment)
            series.add_question(question)
        return series

    def delete_all_series(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from series")
        self._connection.commit()

    def insert_series_questions(self, id_series, id_question):
        cursor = self._connection.cursor()
        sql = """INSERT INTO series_questions(id, id_series, id_question) VALUES (?,?,?)"""
        cursor.execute(
            sql, [self.create_uuid(), id_series, id_question])
        self._connection.commit()

    def delete_all_series_questions(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from series_questions")
        self._connection.commit()

    def delete_all(self):
        self.delete_all_questions()
        self.delete_all_series()
        self.delete_all_series_questions()

    def save_series_data(self, series):
        self.insert_series(series)
        for question in series.questions:
            self.insert_question(question)
            self.insert_series_questions(series.id, question.id)

    def save_question_for_series(self, question, series):
        self.insert_question(question)
        self.insert_series_questions(series.id, question.id)

    def exists_series_name(self, name):
        cursor = self._connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM series WHERE name=?", [name])
        cnt = cursor.fetchone()[0]
        if cnt >= 1:
            return True
        return False


series_repository = SeriesRepository(
    Path(__file__).parent.parent / 'data' / "default_series.csv", get_database_connection())
