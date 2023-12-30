list = [3, 5, 7, "suman", True, None, "89", "999", "harry"]
print(list)
# print(type(list))
# print(list[0])
# print(list[1])
# print(list[-3]) # negative index
# print(list[len(list)- 3]) # positive index

# if 7 in list:
if "suman" in list:
    print("Yes")
else:
    print("No")

# Same thing applies for strings as well!
# if "su" in "suman":
    # print("Yes")

# BY default:- print(list[0:len(list):1])
print(list[2:-1])
print(list[1:-1:2])
print(list[::-1])
print(list[::-2])

# List Comprehension
# lst = [i for i in range(4)]
lst = [(i*i+i) for i in range(6)]
print(lst)

lst1 = [(i*i+i) for i in range(10) if i%2==0]
print(lst1)
