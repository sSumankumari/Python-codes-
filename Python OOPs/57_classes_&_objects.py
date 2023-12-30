# Classes and Objects
class Person:
    name = 'Harry'
    occupation = 'Software Developer'
    networth = 10
    def info(self):
        print(f"{self.name} is a/an {self.occupation}")

# a and b are objects
a = Person()
# a.name = 'John'
b = Person()
b.name = 'Nitika'
b.occupation = 'HR'
# print(a.name, a.occupation)
a.info()
b.info()