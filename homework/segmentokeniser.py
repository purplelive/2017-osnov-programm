import sys

import re

text = sys.stdin.read()


import re



sentenceEnd = re.compile('(?<=(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Dr)(?<!Jr)[:.!?])\s{1,2}(?=[A-Z])')
sentenceList = sentenceEnd.split(text)
index=0
for sentence in sentenceList:

        print('# sent_id = %d' % (index))
        
        print('# text = %s' % (sentence))
        print()
        sentence = sentence.replace(' ', '\n')
        index=index+1
        print(sentence)
        print()
