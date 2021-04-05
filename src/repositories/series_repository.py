from pathlib import Path
from entities.question import Question
from entities.series import Series
import csv

class SeriesRepository:
    
    def __init__(self, file_path):
        self.file_path = file_path

    def get_default_series(self):
        series = Series('default')
        questions = []
        with open(self.file_path) as f:
            reader = csv.reader(f, delimiter=",")
            for i,row in enumerate(reader):
                if i != 0:
                    questions.append(Question(int(row[0]), row[1], row[2]))
        series.set_all_questions(questions)
        return series

series_repository = SeriesRepository(Path(r"/home/juliusni/opiskelu/Ohjelmistotekniikka/ot-harjoitustyo/src/data") / "default_series.csv")
