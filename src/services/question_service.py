from repositories.series_repository import series_repository
from entities.answer import Answer

class QuestionService:
    def __init__(self):
        self.cur_series = None
        self.i_cur_question = None
        self.cur_answers = None

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

    def give_new_answer(self, val):
        answer = Answer(1, self.get_current_question(), val)
        self.cur_answers.append(answer)


    def get_total_score(self):
        return sum([answer.score() for answer in self.cur_answers])



question_service = QuestionService()
question_service.load_default_series()