class User:
    def __init__(self, id_user, name, type_user):
        self.id = id_user
        self.name = name
        self.type = type_user

    def __str__(self):
        return f"User, name: {self.name}, type: {self.type}"
