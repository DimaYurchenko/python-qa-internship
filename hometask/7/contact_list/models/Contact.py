class Contact(object):

    def __init__(self, name: str, number: str, email: str):
        self.name = name
        self.number = number
        self.email = email

    def __str__(self):
        return f'{self.name} {self.number} {self.email}'

    def __repr__(self):
        return f'{self.name} {self.number} {self.email}'
