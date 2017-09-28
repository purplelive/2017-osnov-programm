import sys
import re
text = sys.stdin.read()

for c in text:

    text = text.replace('. ' ,'.\n')
    print(text)
                
