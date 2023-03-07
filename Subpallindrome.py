s='abcba'
for i in range(0,len(s)):
    for j in range(i+1,(len(s)+1)):
        N=s[i:j]
        if N==N[::-1] and len(N)>1:
            print(N)