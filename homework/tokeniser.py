import sys

import re

text = sys.stdin.read()





sentenceEnd = re.compile('(?<=(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Dr)(?<!Jr)[:.!?])\s{1,2}(?=[A-Z])')
sentenceList = sentenceEnd.split(text)
index=1
for sentence in sentenceList:

        print('# sent_id = %d' % (index))
        
        print('# text = %s' % (sentence))
        print()
        
        #wordlist = sentence.replace(' ', ' \n')
        wordEnd = re.compile(' ')
        wordList = wordEnd.split(sentence)
        c=1
        for word in wordList:
             print('%d\t%s\t_\t_\t_\t_\t_\t_\t_\t_' % (c, word))
              
             #print(c,' ',word,'   ', '_','   ', '_','   ', '_','  ', '_', ' ', '_', ' ', '_', ' ', '_')
             
             c=c+1
        
        index=index+1



