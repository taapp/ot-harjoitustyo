class User:
    def __init__(self, id, name, type):
        self.id = id
        self.name = name
        self.type = type
        
    def __str__(self):
        return f"User, name: {self.name}, type: {self.type}"