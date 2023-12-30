def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesser(a, b):
    pass # --> This is used to give body to the function

a = 9
b = 8
isGreater(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
calculateGmean(a, b)
c = 3
d = 9
isGreater(c, d)
calculateGmean(c, d)