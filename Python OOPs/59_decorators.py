# Decorators

def greet(fx):   
    def mfx(*args, **kwargs):
        print('Good Morning')
        fx(*args, **kwargs)
        print('Thanks for using this function')
    return mfx

@greet
def hello():
    print("Hello World")

@greet
def add(a, b):
    print(a + b)
    
hello()
# greet(hello)()
add(2, 3)
# greet(add)(3, 5)