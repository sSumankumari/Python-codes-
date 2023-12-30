def func1():
    try:
        list1 = [1, 5, 6, 7]
        i = int(input("Enter your index: "))
        print(list1[i])
        return 1
    except:
        print("Some error occurred")
        return 0

    finally:
        print("I am always executed")
    # print("I am always executed")

x = func1()
print(x)