import sys

counter = 0 

for c in sys.stdin.read():
	if c in '':
		counter = counter + 1
print(counter)
