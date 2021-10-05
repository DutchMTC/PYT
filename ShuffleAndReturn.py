import random

def rdm(woord):
    return ''.join(random.sample(woord, len(woord)))

print(rdm("random"))
print(rdm("mediacollege"))
print(rdm("bonk"))