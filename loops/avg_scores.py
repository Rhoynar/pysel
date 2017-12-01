scores = [
    9.5,
    8.5,
    7.0,
    9.5,
    10,
    6.5,
    7.5,
    9.0,
    10
]

sum = 0
for score in scores:
    sum += score

average = sum/(len(scores))
print('Average Scores: ' + str(average))
