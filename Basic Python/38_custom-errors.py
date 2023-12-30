# Raising Custom errors
# a = int(input("Enter any value between 5 and 9: "))

# if (a<5 or a>9):
    # raise ValueError("Value should be between 5 and 9")

# Defining Custom Exceptions
class CustomError(Exception):
    # Code
    pass
try:
    # Code
    print()
except CustomError:
    # Code
    print()

num=input("Enter the No.:")
try:
    if 'quit' in num:
        print('Ok')
    elif int(num)>5 and int(num)<9:
        print(num,'Integer Accepted',type(num))
    else:
        print('Value should between 5 and 9')
except:
    raise ValueError('Value is not an Integer.. :')