import sys 
import re

dicts_fd = []
with open('dic.txt','r') as inf: #open file and read it as dictionary
    for line in inf:
        dicts_fd.append(eval(line)) 

text = sys.stdin.read()

sentenceEnd = re.compile('(?<=(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Dr)(?<!Jr)[.!?])\s{1,2}(?=[A-Z])')
sentenceList = sentenceEnd.split(text)
index=1
for sentence in sentenceList:

        print('# sent_id = %d' % (index))
        
        print('# text = %s' % (sentence))
        print()


knights= []       

       for i, w in enumerate(text.split(' ')):
              knights.append((int(i), w))# add the words to the list
       c=1
       for w in knights: #check each word if it is in dictioanary 
              
            if w in dicts_fd.items():# if it is in dic return the catagory of word and print the word and his category 
                   
                  print('%d\t%s\t%s\t_\t_\t_\t_\t_\t_' % (c, w,dicts_fd[w]))
              
             
             
                  c=c+1
        
       index=index+1
                   



     
	

        
       
        
                   
 


