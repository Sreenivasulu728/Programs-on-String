s='PYTHON@123'
res=''
for i in range(0,len(s)):
    if 'A'<=s[i]<='Z':
        res+=chr(ord(s[i])+32)
    else:
        res+=s[i]
print(res)