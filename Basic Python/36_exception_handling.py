# Exception Handling
# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")

# try:
#     for i in range(1, 11):
#         print(f"{int(a)} x {i} = {int(a)*i}")
# except Exception as error:
#     print("error occurred:", error)

# print("Some imp lines of code")
# print("End of program")

try:
    num = int(input("Enter an integer: "))
    a = [3, 7]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error")