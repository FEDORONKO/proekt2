class User:
    """
    Клас представляє користувача додатка.
    """
    def __init__(self, username):
        self.username = username
        self.journal = None

    def create_journal(self):
        from journal import Journal
        self.journal = Journal(self)
        return self.journal