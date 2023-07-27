# WAP to read details n players
# each player is having name and score
# store these player details in dictionary
n = int(input("Enter how many players: "))
players = {}
for i in range(n):
    name = input("Enter Player Name: ")
    score = int(input("Enter Score: "))
    players[name] = score
print(players)