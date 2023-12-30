import os

if(not os.path.exists("46_OS module\data")):
    os.mkdir("46_OS module\data")

for i in range(0, 10):
    os.mkdir(f"46_OS module\data/Day{i+1}")
