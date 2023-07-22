# 1. Write a program that gets two int variables and swaps their values. Do it in 3 different ways.

a = 3
b = 5
a, b = b, a
print("a =", a)
print("b = ", b)


a = 3
b = 5
temp=a
a = b
b=temp 
print("a =", a)
print("b = ", b)


a = 3
b = 5
a = a + b
b = a - b
a = a - b
print("a =", a)
print("b = ", b)

# 2. Write a program that gets 2 numbers from the user. Print to the console their difference. Use the built-in Input function for that

first_digit = int(input("Enter the first number: "))
second_digit = int(input("Enter the second number:  "))
difference = first_digit - second_digit
print("The difference is:", difference)

# 3. Write a program that gets 2 numbers from the user. Print to the console maximum of these two variable. Use a built-in function for that. 

digit1 = 75
digit2 = 34
maximum = max(digit1, digit2)
print("The maximum is:", maximum)