class Series:
    def __init__(self, id_series, name):
        self.id = id_series
        self.name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def set_all_questions(self, questions):
        self.questions = questions

    def print_all_questions(self):
        print("truth, statement:")
        for question in self.questions:
            print(question)

    def __len__(self):
        return len(self.questions)
