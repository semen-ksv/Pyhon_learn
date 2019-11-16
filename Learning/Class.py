class Hero():
    # клас создания героя
    def __init__(self, name, level, race):
        # инициализаця героя
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        # Печать всех параметров героя
        discription = (self.name + ' level is: ' + str(self.level) + ' Rase is: ' + self.race +
                       ' Hels is: ' + str(self.health)).title()
        print(discription)

    def level_up(self):
        # улучшение уровня героя
        self.level += 1

    def mov(self):
        # передвижение героя
        print('Hero ' + self.name + ' srart moving...')

    def set_helth(self, new_health):
        # изменение здоровя героя
        self.health = new_health

class SupperH(Hero):                                    # наследие класа Hero со всеми функциями
    def __init__(self, name, level, race, magiclevel):
        super().__init__(name, level, race)              # super перебрасывает  показатели с супер класа Hero
        self.magiclevel = magiclevel
        self.__mana = 100           # "__" - инкапсуляция, нельзя изменить из вне класачерез "=" только через метод

    def make_magic(self):
        self.__mana -= 10

    def show_hero(self):
        # Печать все параметры героя (такое же название как и в главного класа)
        discription = (self.name + ' level is: ' + str(self.level) + ' Rase is: ' + self.race +
                       ' Hels is: ' + str(self.health) + ' Magic lavel: ' + str(self.magiclevel) +
                       ' Mana: ' + str(self.__mana)).title()
        print(discription)


my_hero1 = Hero("Vurd", 3, 'Ork')
my_hero2 = Hero('Lord', 1, 'Human')

my_hero1.show_hero()
my_hero2.mov()
my_hero1.level_up()
my_hero1.health = 70
my_hero1.show_hero()
my_hero2.set_helth(88)
my_hero2.show_hero()

sup_hero = SupperH('Superman', 8, 'Helian', 7)
sup_hero.show_hero()
sup_hero.make_magic()
sup_hero.make_magic()
sup_hero.show_hero()

print(my_hero1.race)

# --------------------------------------------------------------------------


class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        """some doc"""
        area = self.radius**2 * self.pi
        return area

    def ser_radius(self, new_radius):
        self.radius = new_radius


circul = Circle(radius=100)


print(circul.radius)
print(circul.area())
circul.ser_radius(33)
print(circul.area())

# ====================================================

class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        try:
            self.balance = int(balance)
        except:
            print('input integer')
            self.balance = 0


    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Not enough money')

    def __str__(self):
        return f'Account owner:\t {self.owner}\nAccount balance: {self.balance}$'


acc1 = Account("Bob", 5)
print(acc1)
print(acc1.owner)

print(acc1.balance)
acc1.deposit(50)
print(acc1.balance)
acc1.withdraw(45)
print(acc1.balance)
acc1.withdraw(200)


# =================Dataclass==Total_ordering======


from functools import total_ordering
from dataclasses import dataclass


@dataclass
class Position:
    name: str
    lon: float
    lat: float

    def some(self):
        return self.lon + self.lat
@total_ordering
class Second(Position):

    def __init__(self, name, lon, lat, mon:int):
        self.mon = mon
        super().__init__(name, lon, lat)

    def __eq__(self, other):
        return self.mon == other.mon

    def __lt__(self, other):
        return self.mon < other.mon

    def athe(self):
        return super().some() * self.mon

a = Position(5, 3.5, 5.2)
print(a)
print(a.some())
b = Second('seco', 3.1, 2, 10)

print(b)
print(b.athe())
print(Second.mro())
b.mon = 11
print(b.athe())
c = Second('cop', 2.3,5.2, 5.5)
print(c)
print(c >= b)