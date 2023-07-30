import random

names_list = ["Anna", "Emma", "Mario", "Robert", "Giulia"]
score_list = []

for name in names_list:
    count = 0
    for i in range(100):
        score = random.randint(0, 1000)
        count += score  
    score_list.append((name, count))  

print(score_list)  


import csv

with open('homework_10_3_player_scores.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Player', 'Score'])  
    writer.writerows(score_list)  
