# my first python project ever.

# gonna be about basic arithmatic when user enters numbers

number_1 = int(input("Please Enter a Number between 1 and 9: "))
number_2 = int(input("Please Enter another number between 1 and 9: "))

add = (number_1 + number_2)
subtract = (number_1 - number_2)
multiply = (number_1 * number_2)
divide = (number_1 / number_2)
exponent = (number_1 ** number_2)
modulus = number_1 % number_2



print("Addition:", add)
print("Subtraction:", subtract)
print("Multiplication:", multiply)
print("Division:", divide)
print("Exponent:", exponent)
print("Remainder:", modulus)

# this is to tell user which of their numbers are bigger!
if number_1 > number_2:
    print(number_1, "is larger.")
elif number_2 > number_1:
    print(number_2, "is larger.")
else:
    print("The numbers are equal.")


#avg of numbers
average = (number_1 + number_2) / 2

print("Average:", average)

print("\n-----------------------\n")
print()
print()
print("Thank you for using this program! I hope you enjoyed it!")