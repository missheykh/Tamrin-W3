#1606A AB Balance
t=int(input('enter the number of test cases:'))
j=1
while j<=t:
    s=input('enter a string:')
    c_ab=s.count('ab')
    c_ba=s.count('ba')
    if c_ab==c_ba:
        print(f'AB({s}) is equal to BA({s}) = {c_ba}')
        print(s)
    else:
        print(f'AB({s})={c_ab} , BA({s})={c_ba}')
        if c_ab>c_ba:
            i=s.rfind('ab')
            if s[i-1] != 'a':
                x=s[:i]+'b'+s[i+1:]
            elif s[i-1]=='a':
                x=s[:i+1]+'a'+s[i+2:]
            
        else:
            i=s.rfind('ba')
            if s[i-1]!='b':
                x=s[:i]+'a'+s[i+1:]
            elif s[i-1]=='b':
                x=s[:i+1]+'b'+s[i+2:]
        print(f'Changed String: {x}')
    j+=1
