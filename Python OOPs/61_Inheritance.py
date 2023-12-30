# Inheritance in Python
# Inheritance is a way to reuse code in Python. It allows you to create a new class that inherits the attributes and methods of an existing class. This can save you time and effort, as you don't have to re-write code that has already been written.

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")
        
class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")


e1 = Employee("John", 10627)
e1.showDetails()
e2 = Employee("Jack", 10635)
e2.showDetails()

e3 = Programmer("Harry", 10324)
e3.showDetails()
e3.showLanguage()