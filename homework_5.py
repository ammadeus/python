# 1. Write a program that asks the user to enter an integer and convert it to an int. The program should have 2 functions. 
# The first function should ask the user to input information and return inputted value. The second function receives the inputted value and converts it to int. 
# If the user enters something that is not an integer, this function should catch an error and ask the user to enter an integer again. if the user inputs an integer, 
# the program should print this number and quit w/o any error.


def ent_data():
    data_n = input("Enter an integer: ")
    return data_n
def enter_integer():
    while True:
        data_n = ent_data()
        try:
            number = int(data_n)
            print(number)
            break
        except ValueError:
            print("That was not an integer, try again.")
            
enter_integer()





# 2.Write a program that asks the user to input a string and an integer n. The Program should have 2 functions. 
# The first function should ask the user to enter a string and an integer. The second function should receive the inputted value and print the character at the index n. 
# If the user enters the wrong value, this function should catch an error and provide a proper error message with an explanation.
# After the error is handled, the program should ask the user to enter a string and an integer again. 
# If the user inputs a string and an integer, the program should print the character at the index n and quit w/o any error.


def enter_data():
    user_string = input("Pleace, emter a string : ")
    user_integer = int(input("Pleace, enter integer : "))
    return user_string, user_integer

def print_character_at_index():
    user_string, user_integer = enter_data()
    while True:
        try:
            character = user_string[user_integer]
            print("The character", user_integer, "is:", character)
            break
        except ValueError:
            print("Input not valid.Pleace enter valid string or integer.")
            user_string, user_integer = enter_data()
        except IndexError:
            print("Index out of range. Please enter a valid index.")
            user_string, user_integer = enter_data()

print_character_at_index()


# 3. Transaction
  # a) Define a global variable called balance and set it to 1000. Write a function called transaction that takes an argument amount and argument _type that can be either deposit or withdrawal.              
  # b) Inside the function create two inner functions called deposit and withdrawal that take an argument amount.              
  # c) Inside the deposit function, add the amount to the balance variable and print the new balance.              
  # d) Inside the withdrawal function, subtract the amount from the balance variable and print the new balance.              
  # e) Inside the transaction function, check if the _type argument is deposit or withdrawal and call the appropriate function.




balance = 1000

def transaction(amount, _type):
    if _type == "deposit":
        def deposit():
            global balance
            balance += amount
            print("New balance is:", balance)
        deposit()
    elif _type == "withdrawal":
        def withdrawal():
            global balance
            balance -= amount
            print("New balance is:", balance)
        withdrawal()

transaction(200, "deposit")




# 4. Write a function that simulates a dice roll and returns the result from 1 to 6. Use random module



import random

def roll_dice():
    return random.randint(1, 6)
result = roll_dice()
print("Dice roll result:", result)



# 5. Use the function from the previous task to simulate 1000 dice rolls and print the result. Calculate the number of times each number was rolled.



import random

def roll_dice():
    return random.randint(1, 6)

counts = [0, 0, 0, 0, 0, 0] 

for i in range(1000):
    result = roll_dice()
    counts[result - 1] += 1 

print(counts)



# 6. Simulate an election for two candidates. The program should take the number of regions and the rating for 1st candidate in each region (in percentage).
# The program should run elections in every region. In every region, the program should ask 10 000 voters. Use the random module to simulate a voice from a person. 
# The candidate counts as a winner if he gains more than 50% of all votes. The program should print the result of the election for each region and the winner


import random

def receive_input():
    num_regions = int(input("Enter the number of regions: "))
    ratings = []
    for i in range(num_regions):
        rating = float(input(f"Enter the rating for Candidate 1 in region {i+1} (in percentage): "))
        ratings.append(rating)
    return num_regions, ratings

def simulate_region_election(rating):
    candidate_1_votes = 0
    candidate_2_votes = 0
    for _ in range(10000):
        vote = random.randint(1, 100)
        if vote <= rating:
            candidate_1_votes += 1
        else:
            candidate_2_votes += 1
    return candidate_1_votes, candidate_2_votes

def simulate_election(input_data):
    num_regions, ratings = input_data
    election_results = []
    for i in range(num_regions):
        print(f"Region {i+1}:")
        candidate_1_votes, candidate_2_votes = simulate_region_election(ratings[i])
        election_results.append((candidate_1_votes, candidate_2_votes))
        print("Votes for Candidate 1:", candidate_1_votes)
        print("Votes for Candidate 2:", candidate_2_votes)
    return election_results

def calculate_result(election_results):
    total_candidate_1_votes = 0
    total_candidate_2_votes = 0
    for result in election_results:
        total_candidate_1_votes += result[0]
        total_candidate_2_votes += result[1]
    if total_candidate_1_votes > total_candidate_2_votes:
        winner = "Candidate 1"
    elif total_candidate_2_votes > total_candidate_1_votes:
        winner = "Candidate 2"
    else:
        winner = "No winner (Tie)"
    return winner

def announce_result(result):
    print("Overall Winner:", result)

input_data = receive_input()
election_results = simulate_election(input_data)
result = calculate_result(election_results)
announce_result(result)