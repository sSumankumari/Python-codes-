s1 = {1, 2, 3, 4, 8}
s2 = {4, 8, 12}
# print(s1.union(s2))
# print(s1.intersection(s2))
s1.update(s2)
# print(s1, s2)

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities = cities1.update(cities2)
cities3 = cities1.symmetric_difference(cities2)
# print(cities3)

cities4 = cities2.difference(cities1)
# print(cities4)
# print(cities1.isdisjoint(cities4))
# print(cities1.issubset(cities))
# print(cities.issuperset(cities2))
# cities1.add("Helsinki")
# cities1.remove("Tokyo") #--> This will throw error if the value doesn't match
# cities1.discard("Tokyo2") #--> This will not throw error if the value doesn't match
item = cities1.pop() #--> this will pop out any value from the set
print(item)
print(cities1)
# del(item) #--> del() will delete the set
# print(item)
cities4.clear() #--> clear() will delete all the elements from the set
print(cities4)