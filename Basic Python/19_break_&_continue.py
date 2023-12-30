# Break statement
# for i in range(15):
    # if (i == 10):
        # break
    # print("5 x", i+1, "=", 5 * (i+1))
# print("Break statement applied --> It will leave the loop")

# Continue Statement
# for i in range(15):
    # if (i == 10):
        # print("Skip the iteration")
        # continue
    # print("5 x", i, "=", 5 * (i))
# print("Continue statement applied --> It will leave the iteration")

# Do-while loop using infinite while loop
i = 0
while True:
    print(i)
    i = i + 1
    if(i%10 == 0):
        break