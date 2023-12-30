# Tuples are immutable
countries1 = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries1)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries1 = tuple(temp)
# print(countries1)

countries2 = ("India", "Sri lanka", "Nepal")
countries = countries1 + countries2  # Concatenation
# print(countries)

# count() method --> count the number of occurence of a value
tuple = (1, 0, 6, 3, 1, 2, 1, 3, 7, 1, 3, 3)
res = tuple.count(1)
# print(res)
# print(len(tuple))
# index() method --> Occurence of 1st value at an index
# tup = tuple.index(3)
tup = tuple.index(3, 2, 12)
print(tup)