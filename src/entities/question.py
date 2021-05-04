class Question:
    """Luokka, joka vastaa kysymystä.
    """

    def __init__(self, id_question, truth, statement, comment):
        """Luokan-konstruktori, joka luo uuden kysymyksen.

        Args:
            id_question: Merkkijono, joka on kysymyksen tunniste.
            truth: Kokonaisluku 1 tai 0, joka vastaa kysymysväitteen totuusarvoa.
            statement: Merkkijono, joka vastaa kysymyksen väitettä.
            comment: Merkkijono, joka sisältää kysymykseen liittyvää mahdollista lisätietoa.
        """
        self.id = id_question
        self.truth = truth
        self.statement = statement
        self.comment = comment

    def __str__(self):
        """Palauttaa kysymysolion merkkijonoesityksen.

        Returns:
            Merkkijono, joka sisältää perustietoa kysymyksestä.
        """
        return f'{self.truth}, "{self.statement}"'
