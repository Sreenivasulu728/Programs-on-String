s='engineering'
res=''
for i in range(0,len(s)):
    if s[i] not in res:
        res+=s[i]
print(res)