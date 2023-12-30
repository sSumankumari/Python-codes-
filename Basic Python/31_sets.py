# Sets in Python -> Sets are unchangeable
s = {2, 4, 2, 6, 2}
print(s) #--> It will not take any repeated value

info = {"Carla", 19, False, 5.9 ,19}
print(info) # --> doesn't maintain order

new = {} # Empty dictionary
# new = set() # Empty set
print(type(new))

for value in info: 
    print(value)