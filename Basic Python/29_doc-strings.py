# Doc-strings should be right below the function name otherwise it will work as an string
def square(n):
    '''Takes in a number n, returns the square of n''' #--> This is a doc string
    print(n**2)
square(8)
print(square.__doc__)

# PEP8 --> It stands for Python Enhancement Proposal.
# The Zen of Python --> print it by using 'import this' in the python powershell