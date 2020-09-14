def dup(arry):
    r=[]

    for s in arry:
        ref=s[0]
        d=[]

        for i in range(1,len(s)):
            if (s[i]==ref):
                d.append(i)
            else:
                ref=s[i]

        wL=list(s)

        for i in range(len(d)):
            wL.pop(d[i]-i)
        
        r.append(''.join(wL))

    return r
