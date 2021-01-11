class Role:
    def __init__(self, name: str):
        self.name = name


class User:
    def __init__(self, username: str, email: str, password: str, role: Role):
        self.username = username
        self.email = email
        self.password = password
        self.role = role
