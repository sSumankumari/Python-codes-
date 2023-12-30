# def cube(x):
#     return x*x*x

# print(cube(3))

# ___MAP___
ls = [1, 2, 4, 6, 7, 4]
# newl = []
# for item in l:
#     newl.append(cube(item))

newl = list(map(lambda x: x*x*x, ls))
# print(newl)

# ___FILTER___
# def filter_function(a):
#     return a>3

# filtl = list(filter(filter_function, ls))

filtl = list(filter(lambda a: a>4, ls))
# print(filtl)

# ___REDUCE___
from functools import reduce
num = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
# def mysum(x, y):
#     return x + y
# sum = reduce(mysum, num)
sum = reduce(lambda x, y: x + y, num)

print(sum)