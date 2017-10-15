import sys
from pprint import pprint
from fractions import Fraction

word_tag = {}
tags = {}
word_freq = {}



totaltoken=0

for line in sys.stdin: 
    if '\t' not in line:
        continue
    row = line.split('\t')
    #print(row)
        
    if len(row) != 10:
        continue
    word= row[1]
    if word not in word_freq:
	    word_freq[word] = 0
    word_freq[word] = word_freq[word] + 1
    
    
    if row:
     
       word_tag[row[1]]= row[3]
      
       
    form = row[3]
              
    if form not in tags:
	    tags[form] = 0
    tags[form] = tags[form] + 1
    totaltoken=totaltoken+1   
#pprint(word_tag)
#pprint(totaltoken)
#pprint(tags)
#pprint(word_freq)
counts = {}
for w1 in word_tag:
             
             if w1 not in counts:
                       counts[w1]= {}
                         
        
             for w2 in tags:
                     if word_tag[w1]== w2:
                          for ww in word_freq:
                              if ww == w1:
                                    
                           
                                  counts[w1][w2]= word_freq[ww]
#pprint(counts)                               
p= []

ss = ['#p','count','tag', 'form']
print('\t'.join(ss))

for k,v in tags.items():
     print('%.2f\t %d\t %s\t_'%((v/totaltoken),v,k))

for s in p:     
    print('%d\n\t\t%s\t_\n '%(s),end='')



for s1 in counts:
     print()
     for s2,s3 in counts[s1].items():
          
          print('%.2f\t %d \t%s\t%s'%(counts[s1][s2]/counts[s1][s2],counts[s1][s2],s2,s1))
           
        

      
      











