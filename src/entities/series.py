class Series:
    """Luokka, joka vastaa kysymyssarjaa.

    Attributes:
        id_series: Merkkijono, joka vastaa kysymyssarjan tunnistetta.
        name: Merkkijono, joka vastaa kysymyssarjan nimeä.
        self.questions: Lista, joka sisältää kysymyssarjan kysymykset (Questions-oliot).
    """

    def __init__(self, id_series, name):
        """Konstruktori, joka luo uuden kysymyssarjan.

        Args:
            id_series: Merkkijono, joka vastaa kysymyssarjan tunnistetta.
            name: Merkkijono, joka vastaa kysymyssarjan nimeä.
        """
        self.id = id_series
        self.name = name
        self.questions = []

    def add_question(self, question):
        """Lisää uuden kysymyksen kysymyssarjaan.

        Args:
            question: Question-olio, joka vastaa uutta kysymystä.
        """
        self.questions.append(question)

    def set_all_questions(self, questions):
        """Asettaa annetun kysymyslistan uudeksi kysymyslistaksi.

        Args:
            questions: List-olio, joka sisältää Questions-olioita.
        """
        self.questions = questions

    def print_all_questions(self):
        """Tulostaa kysymyslistan kysymykset.
        """
        print("truth, statement:")
        for question in self.questions:
            print(question)

    def __len__(self):
        """Palauttaa kysymysten määrän listalla.

        Returns:
            Kokonaisluku, joka on kysymyslistan pituus.
        """
        return len(self.questions)

    def empty_questions(self):
        """Tyhjentää kysymyslistan."""
        self.questions = []
