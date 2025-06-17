class UserService:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        self.users[username] = password
        return {"status": "registered"}

    def login_user(self, username, password):
        if self.users.get(username) == password:
            return {"status": "logged in"}
        return {"status": "invalid credentials"}
