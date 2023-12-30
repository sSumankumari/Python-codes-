# String formatting
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Suman"

print(letter.format(country, name))
# print(letter.format(name, country)) # John, India
print(f"Hey my name is {name} and I am from {country}")
print(f"we use f-strings like this: Hey my name is {{name}} and I am from {{country}}")

price = 49.9999
txt = f"For only {price:.2f} dollars!"
# txt = "For only {price:.2f} dollars!" # Using .2f will take two decimal place of a number like (89.99343)
# print(txt.format(price = 49.9999))
print(txt)
print(f"{2 * 30}")
print(type(f"{2 * 30}"))