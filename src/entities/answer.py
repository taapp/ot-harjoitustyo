class Answer:
    def __init__(self, question, probability):
        self.question = question
        self.probability = probability

    def score(self):
        return (self.question.truth - self.probability)**2

    