# readlines() method
f = open('myfile1.txt', 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    # print(f"The mraks of student {i} are: {m1}, {m2}, {m3}")
    # print(f"Marks of student {i} in maths is: {m1}")
    # print(f"Marks of student {i} in physics is: {m2}")
    # print(f"Marks of student {i} in chemistry is: {m3}")
    # print(line)

# writelines() method
f1 = open('myfile3.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f1.writelines(lines)
f1.close()