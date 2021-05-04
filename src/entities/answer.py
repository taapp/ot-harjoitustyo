class Answer:
    """Luokka, joka vastaa kysymykseen annettua vastausta.

    Attributes:
        id_answer: Merkkijono, joka on uuden kysymyksen tunniste.
        question: Question-olio, joka vastaa kysymystä johon vastaus annetaan.
        probability: Lukuarvo, joka vastaa todennäköisyysarviota kysymysväitteen oikeellisuudesta.
    """

    def __init__(self, id_answer, question, probability):
        """Luokan konstruktori, joka luo uuden vastauksen.

        Args:
            id_answer: Merkkijono, joka on uuden kysymyksen tunniste.
            question: Question-olio, joka vastaa kysymystä johon vastaus annetaan.
            probability: Lukuarvo, joka vastaa todennäköisyysarviota kysymysväitteen oikeellisuudesta.
        """
        self.id = id_answer
        self.question = question
        self.probability = probability

    def score(self):
        """Palauttaa vastauksen pisteet.

        Returns:
            Lukuarvo, joka on kysymyksen totuusarvon ja vastauksen todennäköisyysarvion välisen etäisyyden neliö.
        """
        return (self.question.truth - self.probability)**2
