print(3<4)
print(10>5)
print(42==int("42"))



print("Hello everyone")


string = input("Enter string :")
reverse_string = string[::-1]
if string == reverse_string:
    print( "Palindrome" )
else: 
    print( "Not Palindrome" )
   
   
   
name = input("Name : ")
age =  input("Age : ")
you_are_string =  "Your name is {name} and your {age} years old"
print("Your name is Mario and your 55 years old ")
print (you_are_string.format(name=name , age=age))
you_are_string = f"Your name is {name} and your {age} years old"
print(you_are_string)


string_1 = "Animals  "
print(string_1. lower())



string_2 = "  Badger"
print(string_2. upper())


string_3 = "   HoneyPot   "
print(string_3. lstrip())
print(string_3. rstrip())
print(string_3. strip())


string_1 = "Bear"
print(string_1.startswith('Be'))

string_2 = "bear"
print(string_2.startswith('Be'))

string_3 = "BEAR"
print(string_3.startswith('Be'))

string_4 = "bEar"
print(string_4.startswith('Be'))


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