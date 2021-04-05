class Question:
    def __init__(self, id, truth, statement, comment):
        self.id = id
        self.truth = truth
        self.statement = statement
        self.comment = comment
    
    def __str__(self):
        return f'{self.truth}, "{self.statement}"'