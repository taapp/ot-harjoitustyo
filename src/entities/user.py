class User:
    def __init__(self, id_user, name, password, admin):
        self.id = id_user
        self.name = name
        self.password = password
        self.admin = admin

    def __str__(self):
        return f"User, name: {self.name}, type: {self.admin}"
