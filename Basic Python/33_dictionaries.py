# Dictionaries --> ordered collections of key-value pairs
dict1 = {
    101: "Harry",
    102: "John",
    103: "Mary",
    104: "Neha",
    105: "Sunny"
}
# print(dict1)
# print(dict1[102])

info = {'name':'Neha', 'age':19, 'eligible':True}
print(info)
# print(info['name2']) # -->This will throw an error if the key doesn't exist
# print(info.get('eligible2')) # -->And this will not throw any error, only give an output(None)
# print(info.keys()) # --> This is used for accessing multiple keys
# print(info.values()) # --> This is used for accessing multiple values

# for key in info.keys():
    # print(key, ":", info[key])

print(info.items())
for key, value in info.items():
    # print("Key : ", key,"Value : ",value )
    print(f"The value corresponding to the key {key} is {value}")