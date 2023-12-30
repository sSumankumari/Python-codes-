marks = [12, 32, 76, 65, 97, 56, 3, 21]

# index = 0
# for mark in marks:
#     print(mark)
#     if (index == 3):
#         print("Harry, awesome!")
#     index += 1

for index, mark in enumerate(marks):
    print(index, mark)
    if (index == 3):
        print("Harry, awesome!")
    index += 1
