# WAP to read scores of n players
# and find the first maximum and second maximum score

n = int(input("Enter howmany players: "))
scores = []
for i in range(n):
    s = int(input("Enter Score: "))
    scores.append(s)

scores.sort()
# first_maximum
first_max = scores[-1]
# if duplicate value of first_maximum scores are there
c = scores.count(first_max)
# second_maximum
second_max = scores[-(c+1)]
print(f'Scores {scores}')
print(f'First Maximum Score {first_max}')
print(f'Second Maximum Score {second_max}')