
with open("homework_10_2.txt", "r", encoding="utf-8") as homework_10_2:
    content = homework_10_2.read()

content_upper = content.upper()

with open("homework_10_2_copy.txt", "w", encoding="utf-8") as homework_10_2_copy:
    homework_10_2_copy.write(content_upper)