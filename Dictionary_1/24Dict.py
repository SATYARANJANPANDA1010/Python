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
for name,score in players.items():
    print(f'{name} --> {score}')
    total_score = total_score + score
print(f'Total Score is {total_score}')
print(f'Score Board {players}')
