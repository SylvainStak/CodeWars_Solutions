def pairs(ar):
    c,n=0,len(ar)-1 if len(ar)%2==0 else len(ar)-2
    for i in range(0,n,2):
        if(abs(ar[i]-ar[i+1])==1):
            c+=1
    return c