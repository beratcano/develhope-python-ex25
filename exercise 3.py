import random

number1 = random.randint(1,100)
number2 = random.randint(1,100)

print("number1 is: ", number1)
print("number2 is: ", number2)

if number1 > number2:
    print(number1, " is greater than ", number2)
elif number2 > number1:
    print(number2, " is greater than ", number1)
else:
    print(number1, " equals to ", number2)
