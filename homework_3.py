# 1. Make all these expressions True by adding parentheses

bool("False == (not True)")

bool("(True and False) == (True and False)")

bool('(not True) and "A" == "B"')

# 2. Make a solution for Wheat and chessboard problem.

weight_wheat = 0.000065 
chessbord_amount = (2 ** 64 - 1)
weight_amount = weight_wheat * chessbord_amount
print("Wheat weight in tones is " + str(weight_amount))

# 3. Get a positive number from user input.

number = int(input("Enter positive number :  "))
if number > 0:
    print("The factors of" , number , "are: ")
    i = 1
    while (i <= number):
        if(number % i == 0):
            print(i, end = " ")
        i = i + 1
else:
    print("Your numer is not positve.")
    
# 4. Write a Python program to check whether a triangle is equilateral, isosceles or scalene. Get all three sides from user input.

side_a = float(input("Enter side A leight :  "))
side_b = float(input("Enter side B leight :  "))
side_c = float(input("Enter side C leight :  "))

if side_a == side_b and side_b== side_c:
    print("This is equilateral triangle.")
elif side_a != side_b and side_b != side_c and side_a != side_c: 
    print("This is scalene triangle.")
else:
    print("This is isosceles triangle.") 