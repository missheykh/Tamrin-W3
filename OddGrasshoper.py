#1607B Odd Grasshopper
t=int(input('enter the number of test cases:'))
j=1
while j<=t:
    
    x=int(input('x:'))
    n=int(input('n:'))
    i=1
    while i<=n:
        if x%2==0:
            x=x-i
        else:
            x=x+i
        i+=1
    print(x) 
    j+=1

    




