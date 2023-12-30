# Constructors
class Person:
    # name = 'John'
    # occ = 'Developer'
    def __init__(self, name, occ):
        print('Hey I am a person')
        self.name = name
        self.occ  = occ
        
    
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a = Person('John', 'Developer')
b = Person('Divya', 'HR')
# c = Person() # This will give an error as it doesn't have the required no. of arguments

# a.name = 'Divya'
# a.occ = 'HR'
a.info()
b.info()
