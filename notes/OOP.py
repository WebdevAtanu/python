class User:
    name = "",
    age = 0

    # method to display user information
    def showUser(self):
        print(f"The name is {self.name} and age is {self.age}")

user = User()       # creating an object of the User class
user.name = "Ram"   # setting the name attribute of the user object
user.age = 20       # setting the age attribute of the user object
user.showUser()     # calling the showUser method of the user object to display the information

# ==============================================

class Person:
    # constructor method
    def __init__(self, address, phone):
        self.address = address          # setting the address attribute of the Person class
        self.phone = phone              # setting the phone attribute of the Person class

    # method to display person information
    def showPerson(self):
        print(f"Address: {self.address}, Phone: {self.phone}")

p1 = Person("London", '9876543210')     # creating an object of the Person class and passing the address and phone number as arguments to the constructor
p1.showPerson()                         # calling the showPerson method of the p1 object to display the information

# ==============================================

# single inheritance
class Employee(Person): # Employee class inherits from Person class
    def __init__(self, address, phone, salary):     # constructor method of the child class
        super().__init__(address, phone)            # calling the parent class constructor
        self.salary = salary                        # adding new attribute to the child class

    def showEmployee(self):
        print(self.address, self.phone, self.salary)

emp = Employee("America", '9876543210', 50000)      # creating an object of the Employee class and passing the address, phone number and salary as arguments to the constructor
emp.showEmployee()

# ==============================================

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name

    def showDepartment(self):
        print(f"Department Name: {self.dept_name}")

# ==============================================

# multiple inheritance
class Admin(Person, Department):                            # Admin class inherits from both Person and Department classes
    def __init__(self, address, phone, dept_name, role):    # constructor method of the Admin class
        super().__init__(address, phone)                    # calling the constructor of the Person class
        Department.__init__(self, dept_name)                # calling the constructor of the Department class
        self.role = role                                    # adding new attribute to the Admin class

    def showAdmin(self):
        print(self.address, self.phone, self.dept_name, self.role)

admin = Admin("India", '9876543210', "IT", "Manager")
admin.showAdmin()

# ==============================================

# encapsulation and data hiding 
# in Python, we can use a single underscore (_) to indicate that an attribute is intended for internal use (protected) and a double underscore (__) to indicate that an attribute is private and should not be accessed directly from outside the class.
class Product:
    def __init__(self, price):
        self._price = price

    @property               # getter method to access the price attribute
    def price(self):
        return self._price  # returning the value of the price attribute

p = Product(100)
print(p.price)

# ==============================================

# polymorphism
class Shape:
    def area(self):
        pass # this is a placeholder method that will be overridden by the child classes to calculate the area of different shapes

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
shapes = [Rectangle(5, 10), Circle(7)]
for shape in shapes:
    print(shape.area())


