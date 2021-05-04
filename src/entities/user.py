class User:
    """Luokka, joka vastaa sovelluksen käyttäjää.

    Attributes:
        id_user: Merkkijonoarvoa, joka vastaa käyttäjän tunnistetta.
        name: Merkkijono, joka vastaa käyttäjänimeä.
        password: Merkkijono, joka vastaa käyttäjän salasanaa.
        admin: Boolean-arvo, joka kertoo, onko käyttäjä pääkäyttäjä.
    """

    def __init__(self, id_user, name, password, admin):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            id_user: Merkkijonoarvoa, joka vastaa käyttäjän tunnistetta.
            name: Merkkijono, joka vastaa käyttäjänimeä.
            password: Merkkijono, joka vastaa käyttäjän salasanaa.
            admin: Boolean-arvo, joka kertoo, onko käyttäjä pääkäyttäjä.
        """
        self.id = id_user
        self.name = name
        self.password = password
        self.admin = admin

    def __str__(self):
        """Palauttaa käyttäjäolion merkkijonoesityksen.

        Returns:
            Merkkijono, joka sisältää käyttäjän perustiedot.
        """
        return f"User, name: {self.name}, type: {self.admin}"
