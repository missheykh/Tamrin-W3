#1607A Linear Keyboard
t=int(input('enter the number of test cases:'))
print(t)
j=1
while j<=t:
    k=input('enter your keyboard:')
    s=input('enter a world:')
    s=s.lower()
    l=0
    time=0
    while l<len(s)-1:
        
        time+=abs(k.find(s[l+1])-k.find(s[l]))
        l += 1

    print(f'The time for typing your world is: {time}')
    j+=1

