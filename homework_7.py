# 1.  Write a game where the user should guess the capital of the country that you have in your dictionary.

import random

capitals = {
        'Ukraine': 'Kyiv', 'France': 'Paris', 'Germany': 'Berlin',
        'Italy': 'Rome', 'USA': 'Washington', 'Canada': 'Ottawa', 
        'Switzerland': 'Bern', 'Austria': 'Vienna',
        'Belgium': 'Brussels',  'Sweden': 'Stockholm',
        'Norway': 'Oslo', 'Denmark': 'Copenhagen',
        'Finland': 'Helsinki', 'Poland': 'Warsaw',
        'Romania': 'Bucharest', 'Bulgaria': 'Sofia', 'Greece': 'Athens'
}

score = 0

while True:
    random_country = random.choice(list(capitals.keys()))
    capital = capitals[random_country]

    print(f"Guess the capital of the {random_country} or press exit to  to quit the game :")
    guess = input(str())

    if guess.lower() == capital.lower():
        score += 1
        print("You are right!")
    elif guess.lower() == "exit":
        print("You are quit the game. Final score :", score)
        break
    else:
        print("Try again!")

    print("Final score:", score)
    
    
    
# 2. The majority element is the element that appears more than any other element. You may assume that the majority element always exists in the array.
    
    
nums = [2,2,1,1,1,2,2]
def majority_element(nums: list) -> int:
    occurence = {}
    for num in nums:
        if num in occurence:
            occurence[num] += 1
        else: 
           occurence[num] = 1
    majority_element = max(occurence, key=occurence.get)
    return majority_element
majority_element(nums)  


# 3. Find missing subjectsYou are a teacher at a school, and you have just finished grading a set of exams for your students. Each student's exam is represented as a tuple containing their name, their score, and the subject of the exam.
# You want to identify which subjects were not passed by all students so that you can give extra attention to those subjects in your future lessons. Passing is defined as a score of 60 or higher.
# Your task is to write a Python program that reads in a list of student exams, identifies the subjects that were not passed by all students, and outputs a set of those subjects. 


def get_subjects_not_passed_by_all_students(student_exams):
    subjects_not_passed = set()
    subjects_scores = {}

    for name, score, subject in student_exams:
        if subject in subjects_scores:
            if score < subjects_scores[subject]:
                subjects_scores[subject] = score
        else:
            subjects_scores[subject] = score

    for name, score, subject in student_exams:
        if score < 60 and score == subjects_scores[subject]:
            subjects_not_passed.add(subject)

    return subjects_not_passed

def test_get_subjects_not_passed_by_all_students():
    exams = [
        ("Alice", 85, "Math"),
        ("Bob", 59, "Math"),
        ("Charlie", 65, "Math"),
        ("Alice", 90, "Science"),
        ("Bob", 80, "Science"),
        ("Charlie", 32, "Science"),
        ("Alice", 95, "History"),
        ("Bob", 85, "History"),
        ("Charlie", 90, "History"),
    ]
    
    result = get_subjects_not_passed_by_all_students(exams)
    print(result)

    assert get_subjects_not_passed_by_all_students(exams) == {"Science", "Math"}

test_get_subjects_not_passed_by_all_students()
  