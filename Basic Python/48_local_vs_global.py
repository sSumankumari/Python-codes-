x = 4 # global variable

def hello():
    global x # keyword
    x = 44
    y = 8 # local variable
    print(f"The local x is {x}")
    print("Hello, world!")
    print(y)

hello()
print(f"The global x is {x}")
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function