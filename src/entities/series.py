class Series:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def set_all_questions(self, questions):
        self.questions = questions

    def print_all_questions(self):
        print("truth,statement:")
        for q in self.questions:
            print(q)