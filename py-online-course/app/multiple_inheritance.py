# Inheritance (Herança)

class Animal:
    def __init__(self, name: str):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Cat(Animal):
    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

class CatDog(Cat, Dog):
    def run(self):
        print(f"{self.name} is running")


cat = Cat(name='Mimi')
print(cat.name)
print(cat.eat())
print(cat.sleep())

dog = Dog(name='Meggy')
print(dog.name)
print(dog.eat())
print(dog.bark())

cat_dog = CatDog("Kitpes")
cat_dog.eat()
cat_dog.sleep()
cat_dog.bark()
cat_dog.run()
print(dir(cat_dog))






