import os
folders = os.listdir("46_OS module/data")

# print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"46_OS module/data/{folder}"))