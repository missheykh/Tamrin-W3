# 1606A Era
import random
t=int(input('enter the number of Test cases:'))
j=1
while j<=t:
    n=int(input('enter the length of sequenc:'))
    s=input('enter the sequence of numbers:')
    s=s.split()
    count=0
    i=0
    while s and i<len(s):

        if  int(s[i])>i+1:
            s.insert(i,str(random.randint(1,i+1)))
            count+=1
        i+=1

    print(count)
    j+=1




    

