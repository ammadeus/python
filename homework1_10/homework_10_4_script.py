import csv

with open('homework_10_3_player_scores.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  
    scores_data = list(reader)  

high_scores = {}
for name, score in scores_data:
    score = int(score)
    if name in high_scores:
        if score > high_scores[name]:
            high_scores[name] = score
    else:
        high_scores[name] = score

sorted_high_scores = sorted(high_scores.items(), key=lambda x: x[1], reverse=True)

with open('homework_10_4_high_scores.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Player', 'High Score'])  
    writer.writerows(sorted_high_scores) 
