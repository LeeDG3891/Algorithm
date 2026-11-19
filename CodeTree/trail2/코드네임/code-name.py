MAX_N = 5

class Agent:
    def __init__(self, name, score):
        self.name = name
        self.score = score

users = []
for _ in range(MAX_N):
    codename, score = input().split()
    users.append(Agent(codename, int(score)))

min_user = users[0]
for user in users:
    if user.score < min_user.score:
        min_user = user

print(min_user.name, min_user.score)