class Answer:
    def __init__(self, id_answer, question, probability):
        self.id = id_answer
        self.question = question
        self.probability = probability

    def score(self):
        return (self.question.truth - self.probability)**2
