n = int(input())
players = [input().split()for i in range(n)]
winners = [player[0] for player in players if player[1] == 'win']
print(winners)
print(len(winners))
