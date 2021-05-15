from repositories.series_repository import series_repository
from repositories.user_repository import user_repository
from entities.series import Series
from entities.question import Question
from entities.answer import Answer
from entities.user import User
import uuid


class QuestionService:
    """Sovelluslogiikkaa sisältävä luokka"""

    def __init__(self):
        """[summary]
        """
        self.cur_series = None
        self.i_cur_question = None
        self.cur_answers = None
        self.cur_user = None
        self.list_series = None
        self.list_questions = None

    def load_default_series(self):
        """Lataa default-kysymyssarjan ja alustaa vastausattribuutit.
        """
        print("QuestionService, load_default_series")
        self.cur_series = series_repository.get_default_series()
        self.i_cur_question = None
        self.cur_answers = []

    def load_series_by_id(self, id_series):
        self.cur_series = series_repository.get_series(id_series)
        self.i_cur_question = None
        self.cur_answers = []

    def load_series_by_name(self, name):
        self.cur_series = series_repository.get_series_by_name(name)
        self.i_cur_question = None
        self.cur_answers = []

    def load_all_series(self):
        self.list_series = series_repository.get_series_all()

    def load_all_questions(self):
        self.list_questions = series_repository.get_questions_all()

    def get_current_question(self):
        """Palauttaa tällä hetkellä vuorossa olevan kysymyksen.

        Returns:
           Vuorossa listalla olevan Question-olion.
        """
        return self.cur_series.questions[self.i_cur_question]

    def get_next_question(self):
        """Palauttaa seuraavana vuorossa olevan kysymyksen sekä kasvattaa kysymysindeksiä.

        Returns:
            Palauttaa listalla seuraavan Question-olion tai None, jos seuraavaa kysymystä ei ole.
        """
        if self.i_cur_question is None:
            self.i_cur_question = 0
        else:
            self.i_cur_question += 1
        if self.is_series_finished():
            return None
        return self.get_current_question()

    def is_series_finished(self):
        """Kertoo, onko käsiteltävässä kysymyssarjassa enää jäljellä kysymyksiä.

        Returns:
            Boolean-arvon True, jos kysymyksiä ei ole enää jäljellä.
        """
        return self.i_cur_question >= len(self.cur_series)

    def add_answer(self, answer):
        """Lisää vastauksen käsittelyssä olevaan vastauslistaan.

        Args:
            answer: Answer-olio
        """
        self.cur_answers.append(answer)

    def give_new_answer(self, val):
        """Luo käsittelyssä olevalle kysymykselle vastausolion ja lisää sen vastauslistalle.

        Args:
            val: Numeroarvo, joka vastaa annetun vastauksen todennäköisyysarvoa.
        """
        answer = Answer(self.create_uuid(), self.get_current_question(), val)
        self.add_answer(answer)

    def get_total_score(self):
        """Palauttaa kokonaispistemäärän (pisteiden keskiarvon) käsittelyssä oleville vastauksille.
        Jos käsittelyssä ei ole yhtään vastausta, palautetaan None.

        Returns:
            Palautetaan numeroarvo, joka vastaa kokonaispistetulosta eli Brier-pisteytystä,
            tai palautetaan None, jos käsittelyssä ei ole yhtään vastausta.
        """
        if len(self.cur_answers)==0:
            return None
        return sum([answer.score() for answer in self.cur_answers])/len(self.cur_answers)

    def create_uuid(self):
        """Luo uuden uuid:n.

        Returns:
            Merkkijono, joka on luotu uuid.
        """
        uuid_new = str(uuid.uuid4())
        return uuid_new

    def create_user(self, username, password, is_admin):
        """Luo uuden käyttäjän.

        Args:
            username: Merkkijono, joka vastaa käyttäjänimeä.
            password: Merkkijono, joka vastaa salasanaa.
            is_admin: Boolean-arvo, joka kertoo onko uusi käyttäjä pääkäyttäjä.

        Returns:
            User-olio, joka vastaa uutta käyttäjää.
        """
        uuid_user = self.create_uuid()
        user = User(uuid_user, username, password, is_admin)
        return user

    def save_user(self, username, password, is_admin):
        """Luo ja tallentaa uuden käyttäjän, jos samaa käyttäjänimeä ei ole vielä olemassa.

        Args:
            username: Merkkijono, joka vastaa käyttäjänimeä.
            password: Merkkijono, joka vastaa salasanaa.
            is_admin: Boolean-arvo, joka kertoo onko uusi käyttäjä pääkäyttäjä.

        Returns:
            Boolean-arvo, jonka arvo on False, jos sama käyttäjänimi on jo olemassa, ja True muussa tapauksessa.
        """
        if self.exists_username(username):
            return False
        user_new = self.create_user(username, password, is_admin)
        user_repository.insert_user(user_new)
        return True

    def load_user(self, username, password):
        """Lataa tallennetun käyttäjän.

        Args:
            username: Merkkijono, joka vastaa käyttäjänimeä.
            password: Merkkijono, joka vastaa salasanaa.

        Returns:
            User-olion, jos käyttäjä on olemassa, tai None, jos käyttäjää ei ole olemassa.
        """
        return user_repository.load_user(username, password)

    def set_current_user(self, user):
        """Asettaa käyttäjän nykyiseksi käyttäjäksi.

        Args:
            user: User-olio, joka asetetaan nykyiseksi käyttäjäksi.
        """
        self.cur_user = user

    def exists_username(self, username):
        """Kertoo, onko annettu käyttäjänimi tallennettu aikaisemmin.

        Args:
            username: Merkkijono, joka vastaa käyttäjänimeä.

        Returns:
            Boolean-arvo, joka kertoo, onko käyttäjänimi tallennettu aiemmin.
        """
        return user_repository.exists_username(username)

    def load_and_set_user(self, username, password):
        """Lataa käyttäjätiedot ja asettaa tietoja vastaavan käyttäjän nykyiseksi käyttäjäksi.

        Args:
            username: Merkkijono, joka vastaa käyttäjänimeä.
            password: Merkkijono, joka vastaa salasanaa.
        """
        user = self.load_user(
            username, password)
        self.set_current_user(user)

    def current_user_is_admin(self):
        if self.cur_user is None:
            return None
        return self.cur_user.admin

    def create_series(self, name):
        """Luo uuden kysymyssarjan.

        Args:
            name: Merkkijono, joka vastaa kysymyssarjan nimeä.

        Returns:
            Series-olio, joka vastaa uutta kysymyssarjaa.
        """
        uuid_series = self.create_uuid()
        series = Series(uuid_series, name)
        return series

    def exists_series_name(self, name):
        """Kertoo, onko annettu kysymyssarjan nimi tallennettu aikaisemmin.

        Args:
            name: Merkkijono, joka vastaa kysymyssarjan nimeä.

        Returns:
            Boolean-arvo, joka kertoo, onko kysymyssarjan nimi tallennettu aiemmin.
        """
        return series_repository.exists_series_name(name)

    def save_series(self, name):
        """Luo ja tallentaa uuden kysymyssarjan, jos samaa kysymyssarjaa ei ole vielä olemassa.

        Args:
            name: Merkkijono, joka vastaa kysymyssarjan nimeä.

        Returns:
            Boolean-arvo, jonka arvo on False, jos sama kysymyssarja on jo olemassa,
            ja True muussa tapauksessa.
        """
        if self.exists_series_name(name):
            return False
        series_new = self.create_series(name)
        series_repository.insert_series(series_new)
        return True

    def set_current_series(self, series):
        """Asettaa kysymyssarjan käsiteltäväksi kysymyssarjaksi

        Args:
            series: Series-olio, joka vastaa käsittelyyn menevää kysmyssarjaa

        Returns:
            Series-olio, joka on nyt käsittelyssä
        """
        self.cur_series = series
        return series

    def empty_current_series(self):
        """Asetetaan, että kysymyssarjaa ei ole käsittelyssä"""
        self.cur_series = None

    def create_question(self, truth, statement, comment):
        """Luo uuden kysymyksen.

        Args:
            truth: Kokonaisluku, jonka arvo 0 tai 1, joka vastaa kysymysväitteen totuusarvoa.
            statement: Merkkijono, joka vastaa kysymyksen väitettä.            
            comment: Merkkijono, joka vastaa kysymyksen kommenttia.

        Returns:
            Series-olio, joka vastaa uutta kysymyssarjaa.
        """
        uuid_series = self.create_uuid()
        question = Question(uuid_series, truth, statement, comment)
        return question


    def save_question(self, truth, statement, comment):
        """Luo uuden kysymyksen ja tallentaa sen käsittelyssä olevalle kysymyssarjalle.

        Args:
            truth: Kokonaisluku, jonka arvo 0 tai 1, joka vastaa kysymysväitteen totuusarvoa.
            statement: Merkkijono, joka vastaa kysymyksen väitettä.
            comment: Merkkijono, joka vastaa kysymyksen kommenttia.
        """
        question = self.create_question(truth, statement, comment)
        print(f"QuestionService, save_question, question: {question}, self.cur_series: {self.cur_series}")
        series_repository.save_question_for_series(question, self.cur_series)


question_service = QuestionService()
#question_service.load_default_series()
