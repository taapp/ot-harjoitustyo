from repositories.series_repository import series_repository
from repositories.user_repository import user_repository
from entities.answer import Answer
from entities.user import User
import uuid


class QuestionService:
    def __init__(self):
        self.cur_series = None
        self.i_cur_question = None
        self.cur_answers = None
        self.cur_user = None

    def load_default_series(self):
        self.cur_series = series_repository.get_default_series()
        #self.i_cur_question = 0
        self.cur_answers = []

    def get_current_question(self):
        return self.cur_series.questions[self.i_cur_question]

    def get_next_question(self):
        if self.i_cur_question is None:
            self.i_cur_question = 0
        else:
            self.i_cur_question += 1
        if self.is_series_finished():
            return None
        return self.get_current_question()

    def is_series_finished(self):
        return self.i_cur_question >= len(self.cur_series)

    def add_answer(self, answer):
        self.cur_answers.append(answer)

    def give_new_answer(self, val):
        answer = Answer(self.create_uuid(), self.get_current_question(), val)
        self.add_answer(answer)

    def get_total_score(self):
        return sum([answer.score() for answer in self.cur_answers])/len(self.cur_answers)

    def create_uuid(self):
        uuid_new = str(uuid.uuid4())
        return uuid_new

    def create_user(self, username, password, is_admin):
        uuid_user = self.create_uuid()
        user = User(uuid_user, username, password, is_admin)
        return user

    def save_user(self, username, password, is_admin):
        user_new = self.create_user(username, password, is_admin)
        user_repository.insert_user(user_new)

    def load_user(self, username, password):
        return user_repository.load_user(username, password)

    def set_current_user(self, user):
        self.cur_user = user

    def load_and_set_user(self, username, password):
        user = self.load_user(
            username, password)
        self.set_current_user(user)


question_service = QuestionService()
question_service.load_default_series()
