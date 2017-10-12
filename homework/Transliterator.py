import sys
import re


def get_translations(file):
    """
      >>> get_translations(["from to"])
      {'from': 'to'}
     """
    d = {}
    for line in file:
        line = line.strip()
        if line:
            key, value = line.split(' ')
            d[key] = value
    return d

with open('alphabet.txt') as inf:
    trans = get_translations(inf)

text = sys.stdin.read()

sentenceEnd = re.compile('(?<=(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Dr)(?<!Jr)[.!?])\s{1,2}(?=[A-Z])')
sentenceList = sentenceEnd.split(text)
index=1
for sentence in sentenceList:
        print('# sent_id = %d' % (index))
        
        print('# text = %s' % (sentence))
        print()

       
        knights = []     
        for i, w in enumerate(sentence.split(' ')):
              knights.append(w)
        i=1    
        for w in knights:
              
              chars = []
              for c in w:
                   

                   if c in trans:
                       
                       chars.append(trans[c])
              
                       ''.join(chars)
                       
              print('%d\t%s \t_\t_\t_\t_\t_\t_\t_\ttranslate=%s '%(i,w,''.join(chars)))
              i=i+1
             


               
                   
       
        index=index+1
