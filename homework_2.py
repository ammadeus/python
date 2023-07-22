# 1.Make all these expressions true.

print(3 < 4)
print(10 > 5)
print(42 != "42")

# 2. Print the text in which there will be a quote with double quotes.

print("Hello everyone")

# 3. Get a string from user input. Check if the string is a palindrome.

string = input("Enter word :")
reverse_string = string[::-1] 
result = "palindrme" * (string == reverse_string) or "not palindrome"
print("Tne word", string, "is", result + ".")

 # 4. The program receives the user's name and age from the input. Then you need to display the name and age in one line in several ways:
 
name = input("Name : ")
age =  input("Age : ")
you_are_string =  "Your name is {name} and your {age} years old"
print("Your name is Mario and your 55 years old ")
print (you_are_string.format(name=name , age=age))
you_are_string = f"Your name is {name} and your {age} years old"
print(you_are_string)

# 5. Format string with proper built-in function
    # All letters must be written in lowercase.
    
string_1 = "Animals  "
print(string_1. lower())

    # All letters must be capitalized.
    
string_2 = "  Badger"
print(string_2. upper())

    #  Remove all spaces:
    
string_3 = "   HoneyPot   "
print(string_3. lstrip())
print(string_3. rstrip())
print(string_3. strip())

# 6. Check the value of the startwith('Be') function for each line.:

string_1 = "Bear"
print(string_1.startswith('Be'))

string_2 = "bear"
print(string_2.startswith('Be'))

string_3 = "BEAR"
print(string_3.startswith('Be'))

string_4 = "bEar"
print(string_4.startswith('Be'))

# 7. Convert these bear-like rows with methods from the previous exercise to have a positive result for each row

string_1 = "Bear" 
formatted_string1 = string_1.capitalize()
formatted_string1.startswith('Be')

string_2 = "bear" 
formatted_string2 = string_2.capitalize()
formatted_string2.startswith('Be')

string_3 = "BEAR" 
formatted_string3 = string_2.capitalize()
formatted_string3.startswith('Be')

string_4 = "bEar" 
formatted_string4 = string_2.capitalize()
formatted_string4.startswith('Be')