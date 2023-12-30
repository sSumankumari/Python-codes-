# "is" --> exact location of object in memory
# "==" --> equality of the value of any 2 objects
# Both are used for comparison
a = 4
b = "4"

print(a is b)
print(a == b)

c = [1, 2, 12]
d = [1, 2, 12]
print(c is d) # This is false because list is mutable
print(c == d)