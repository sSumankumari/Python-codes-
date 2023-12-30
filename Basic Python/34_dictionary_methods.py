# Dictionary Methods
ep1 = {102: 45, 103: 78, 104: 57, 105: 98}
ep2 = {502: 82, 503: 61}

# ep1.update(ep2) # update() method updates the value of the key provided to it
# ep1.clear() # clear() removes all the items
# ep1.pop(104) # removes the key:value pair whose key is passed
ep1.popitem() # removes the last key:value pair
# del ep1[103] # deletes a dictionary item
print(ep1)
empt = {} # Empty dictionary

# Resource --> docs.python.org