import sys 
a=0

for c in sys.stdin.read():
        print('main loop:',a, c, file = sys.stderr )
        if c in 'eioöüuı':
                print('found a vowel', c, file = sys.stderr)
                a=a+1
print(a)
