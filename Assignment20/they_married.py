import random

boys = ['mohammad', 'sobhan', 'abdollah', 'kiya', 'mahdi', 'sajjad', 'homan', 'arman']
girls = ['mahtab', 'hane', 'harir', 'fateme', 'kiana', 'faezeh', 'minoo', 'mina', 'soghra']

results = []

while len(boys) > 0 and len(girls) > 0:
    boy = random.choice(boys)
    girl = random.choice(girls)
    results.append((boy, girl))
    boys.remove(boy)
    girls.remove(girl)

print(results)
