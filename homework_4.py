# 1. Write a function called `find_primes` that takes in two integers a and b and returns a list of all the prime numbers between a and b (inclusive)


a = 7
b = 156

def find_primes(a :int, b :int):
    return(find_primes)
    
 
for num in range(a, b + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break  
            else:
                print( num) 

          
          
# 2. Write a function called `unique_characters` that takes in a string s and returns a Boolean value indicating whether or not all the characters in s are unique.

          
def unique_characters(string: str):
    unique_chars = set(string)
    return len(unique_chars) == len(string)

string = str(input("Press :"))

if unique_characters(string):
    print("Characters are unique.")
else:
    print("Characters are not unique.")
 
 
    
#  3. Write a function that calculates [Fibonacci series](https://en.wikipedia.org/wiki/Fibonacci_sequence). 

      
def fibonacci(n: int):
  if n in {0, 1}:
      return n
  return fibonacci(n - 1) + fibonacci(n - 2)
x = int(input("Enter Fibonacci sequence: "))
for n in range(15):
    result = fibonacci(n)
    print(result)
    


# 4. Write a function that implements case swapping. It should return the same result as swapcase() method. Your function should accept one str argument and convert all lower case values to upper case and vice versa.


string = str(input("Enter your string : "))
new_string = str()

for i in string:
    if i.isupper():
        i = i.lower()
        new_string += i
    else:
        i = i.upper()
        new_string += i

print(new_string)
 
 
    
 
# 5. Write a function that calculates the performance of a deposit in a bank account. The function called simple_interest takes three arguments: the initial amount, the annual interest rate (as a float), and the time in years.   
 
    
def calculate_deposit_performance(initial_amount, interest_rate, years):
    total_amount = initial_amount
    for _ in range(years):
        interest = total_amount * interest_rate
        total_amount = total_amount + interest
    return total_amount

initial_amount = int(input("Enter initial amount : "))
interest_rate = float(input("Enter your interest rate : "))
years = int(input("Indicate for hove many years you live your amount : "))

performance = calculate_deposit_performance(initial_amount, interest_rate, years)
print("Total amount after", years, "years:", performance)
    
    
    
    
    
      