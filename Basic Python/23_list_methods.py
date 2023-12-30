list = [3, 5, 7, "suman", True, None, "89", "999", "harry"]
# print(list)
# list.append(28) # append() adds a value at the end of the list
# print(list)


list1 = [99, 67, 89, 3, 72, 12]
# list1.sort() # --> It arranges the list in ascending order
# list1.sort(reverse = True) # --> It arranges the list in decending order
# list1.reverse() # --> It modifies the list in reverse order
# print(list1.index(67)) # --> It gives the position(index) of the modified list
# print(list1)
# print(list1.count(67)) # --> It counts the number of value occurence

# m = list1 # -->reference --> this will modify the list
# m = list1.copy() # --> This will not modify the list
# m[0]= 34
# list1.insert(1, 676) # insert(index, value)
print(list1)

n = [900, 677, 1010]
k = list1 + n # Concatenation
print(k)
list1.extend(n) # --> It adds more values to the list
print(list1)