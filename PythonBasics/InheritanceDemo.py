# class BaseClass:
#   Body of base class
# class DerivedClass(BaseClass):
#   Body of derived class

Creating the parent class
class Employee:
    def __init__(self,empname, emproll):
        self.empname= empname
        self.emproll = emproll

    def getdetails(self):
        print(self.empname)
        print(self.emproll)
Creating the child1 class

class QA(Employee):
    def __init__(self,dept,empname, emproll):
        self.dept = dept
        Employee.__init__(self,empname, emproll)

    def getdept(self):
        print(self.getdetails)
# Creating the child2 class


class DEV(Employee):
    def __init__(self, dept, empname, emproll):
        self.dept = dept
        Employee.__init__(self, empname, emproll)

    def getdept(self):
        print(self.dept)
# Creating the object for child class


obj1 = QA("Automation","Ram",1)
obj1.getdetails()
obj1.getdept()


obj2 = DEV("Developer","Kumar",2)
obj2.getdetails()
obj2.getdept()