# Lambda function --> an anonymous function
# def double(x):
    # return x * 2

double = lambda x: x*2
cube = lambda x: x*x*x

print("Double of a number is:",double(5)) # Output: Double of the
print(cube(6))

# For 2 variables
avg = lambda x, y: (x + y) / 2
print(avg(7, 9))

def appl(fx, value):
    return 6 + fx(value)
print(appl(cube, 2))
print(appl(lambda x: x*x, 3))