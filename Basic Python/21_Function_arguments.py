def average(a=9, b=3):
    # print("The average is", (a+b)/2)
    return (a+b)/2

p = average(0,4) # Calling a function
print(p)

# average(5, 3)
# average(6)
# average(b=8)

# def name(fname, mname = "John", lname = "Newton"):
    # print("Hello,", fname, mname, lname)
# name("Amy", "Jack", "Tommy")

# average(b=9, a=21)

def average1(a, b=9):
    print("The average is ", (a+b)/2)
# average1(7)

def newAverage(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))

newAverage(5, 5, 5, 7, 8)