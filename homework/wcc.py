import sys

tokens = 0
lines = 0
characters = 0 

for c in sys.stdin.read():
    if c =='':
        tokens = tokens + 1
    if c =='\n':
        lines= lines +1
    characters = characters+1

print(tokens, lines, characters)
