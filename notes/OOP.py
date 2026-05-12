class User:
    name = "",
    age = 0

    def getInfo(self):
        print(f"The name is {self.name} and age is {self.age}")

user = User()
user.name = "Ram"
user.age = 20
user.showUser()

class Person:
    # constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)

p1 = Person("Atanu", 25)
p1.show()

# inheritance
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display(self):
        print(self.name, self.age, self.salary)

emp = Employee("Dev", 30, 50000)
emp.display()

# encapsulation and data hiding 
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

p = Product(100)
print(p.price)