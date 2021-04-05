class Answer:
    def __init__(self, id, question, probability):
        self.id = id
        self.question = question
        self.probability = probability

    def score(self):
        return (self.question.truth - self.probability)**2

    