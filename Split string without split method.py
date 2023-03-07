s='we are groot'
ss=''
l=[]
for i in range(0,len(s)):
    if s[i]!=' ':
        ss+=s[i]
    else:
        l.append(ss)
        ss=''
l.append(ss)
print(l)

