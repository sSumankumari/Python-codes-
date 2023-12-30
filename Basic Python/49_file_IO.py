# File Handling in Python

# Reading a file
# file1 = open('myfile.txt', 'r')
# print(file1)
# text1 = file1.read()
# print(text1)
# file1.close()

# Writing to a file
# file2 = open('myfile2.txt', 'w')
# file2.write('Hello world!')
# file2.close()

# Appending in a file
# file3 = open('myfile2.txt', 'a')
# file3.write('Hello, Hello')
# file3.close()

with open('myfile.txt', 'a') as f:
    f.write("\nHey I'm inside with")