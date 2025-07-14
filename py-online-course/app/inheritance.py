# Inheritance (Herança)

class Animal:
    def __init__(self, name: str):
        self.name = name

    def eat(self):
        return "eating"

class Cat(Animal):
    def meow(self):
        return "meow"


class Dog(Animal):
    def bark(self):
        return "auau"


cat = Cat(name='Mimi')
print(cat.name)
print(cat.eat())
print(cat.meow())

dog = Dog(name='Meggy')
print(dog.name)
print(dog.eat())
print(dog.bark())





