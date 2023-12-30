tup = (1, 5, 7 , "yellow", True, None)
# tup[0] = 90 # --> This will throw an error
# print(type(tup))
# print(len(tup))
# print(type(tup), tup)
# print(tup[1])
print(tup[-2])
print(tup[-2::-1])
# print(type(tup[3]))

if 7 in tup:
    print("Yes")

tup1 = tup[1:4]
print(tup1)