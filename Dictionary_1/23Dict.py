# WAP to read details n players
# each player is having name and score
# store these player details in dictionary
# and find total score
n = int(input("Enter how many players: "))
players = {}
for i in range(n):
    name = input("Enter Player Name: ")
    score = int(input("Enter Score: "))
    players[name] = score
total_score = 0
for s in players:
    total_score = total_score + players[s]
print(f'Score Board {players}')
print(f'Total Score is {total_score}')
