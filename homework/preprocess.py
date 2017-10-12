import sys

text = sys.stdin.read()

for c in text:
   
     text = text.replace(':', ' :')
     text = text.replace(')', ' )')
     text = text.replace('(', '( ')
     text = text.replace('. ', ' . ')
     text = text.replace('"', ' "')
     text = text.replace(',', ' ,')
     text = text.replace('"', '" ')
     text = text.replace('",', '",')
     print(text)
     break
