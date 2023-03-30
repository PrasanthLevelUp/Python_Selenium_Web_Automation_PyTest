# Python Objects and Classes
"""class ClassName:
    # Statement"""


Defining a Class in Python
class Student:
    name = "Ram"
    rank = 1

    def show(self):
        print(self.name)
        print(self.rank)


Creating an Object in Python
student1 = Student()
print(student1.rank)
student1.show()


# Constructors in Python
class Car:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(self.name)
        print(self.price)


bmw = Car("bmw", 100000)
bmw.show()
benz = Car("benz", 200000)
benz.show()
