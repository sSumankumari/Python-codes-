# Strings are immutable
a = "!!Hello World &&!!!!!"
# print(a)
# print(len(a))
# print(a.upper())
# print(a.lower())

# print(a.rstrip("!"))
# print(a.lstrip("!"))

# print(a.replace("World", "John"))
# print(a.split(" "))

blogHeading = "introduction tO JS"
# print(blogHeading.capitalize())

str1 = "Welcome_to_the_Console!!!"
# print(len(str1))
# print(str1.center(50))
# print(len(str1.center(40)))
# print(a.count("!"))
# print(str1.endswith("!!"))
# print(str1.endswith("to", 4, 10))

# print(str1.find("to"))
# print(str1.find("is"))
# print(str1.index("is"))

str2 = "welcome7"
# print(str2.isalnum())
# print(str2.isalpha())
# print(str2.islower())
print(str2.isprintable())

str3 = "HelloHellohello\n"
print(str3.isprintable())
str4 = "   "
print(str4.isspace())

str5 = "World Health Organization"
print(str5.istitle())

str6 = "Hii this is me"
print(str6.startswith("Hii"))
print(str6.swapcase())
print(str6.title())