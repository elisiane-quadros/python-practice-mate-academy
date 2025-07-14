#Inheritance

class User:
    role = "user"

    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age

    def info(self) -> str:
        return f"{self.name} is {self.age} years old"

class Admin(User):
    role = "admin"

    def __init__(self, name: str, surname: str):
        super().__init__(name=name)
        self.surname = surname

    def info(self) -> str:
        return f"{self.name} {self.surname}"

    def auth(self):
        return f"{self.name} is authorized"

john: User = User(name="John", age=30)
print(john.__dict__)
print(john.info())

# print(dir(john))
peter: Admin = Admin(name="Peter", surname="Packer")
print(peter.__dict__)
print(peter.info())