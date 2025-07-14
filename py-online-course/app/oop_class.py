#What is OOP in Python?


bonus_coef = 1.1

def calculate_salary(salary: float) -> float:
    return salary * bonus_coef

print(calculate_salary(salary=300))



class Employee:
    bonus_coef = 1.1

    def __init__(self, salary: float):
        self.salary = salary #atributte

    def calculate_salary(self) -> float:
        return self.salary * Employee.bonus_coef #method

john: Employee = Employee(salary=500)
print(john.calculate_salary())