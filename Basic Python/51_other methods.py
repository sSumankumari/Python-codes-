# with open('myfile2.txt', 'r') as f2:
    # print(type(f2))
    # Move to the 10th byte in the file
    # f2.seek(10)

    # Read the next 5 bytes
    # print(f2.tell())
    # data = f2.read(5)
    # print(data)

with open('sample.txt', 'w') as f2:
    f2.write('Hello world!')
    # f2.truncate(3)
    