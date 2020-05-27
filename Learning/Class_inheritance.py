from abc import ABCMeta, abstractmethod

class Saveable(metaclass=ABCMeta):

    def save(self):
        Database.insert(self.to_dict())

    @abstractmethod
    def to_dict(self):
        pass


class User(Saveable):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        return 'Logged in!'

    def __repr__(self):
        return f'User {self.username}'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
        }


class Admin(User):
    def __init__(self, username, password, access):
        super(Admin, self).__init__(username, password)
        self.access = access

    def __repr__(self):
        return f'Admin {self.username}, access {self.password}'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'access': self.access
        }

class Database:

    content = {'users': []}

    @classmethod
    def insert(cls, data):
        cls.content['users'].append(data)

    @classmethod
    def remove(cls, finder):
        cls.content['username'] = [user for user in cls.content['users'] if finder(user)]

    @classmethod
    def find(cls, finder):
        return [user for user in cls.content['users'] if finder(user)]

a = Admin('Rolf', '1234', 3)

c = Admin('Bol', '234', 2)



class Store(User):
    def __init__(self, name, address):
        super(User, self).__init__()

        self.name = name
        self.address = address

    def to_dict(self):
        return {
            'name': self.name,
            'address': self.address,
        }

b = Store('Mol', 'Kiev')

users = [a,b,c]
for user in users:
    user.save()

print(Database.content)