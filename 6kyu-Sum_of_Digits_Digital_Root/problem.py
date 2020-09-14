def digital_root(n):
    r=str(n)

    while(len(r)!=1):
        t=0
        for i in r:
            t+=int(i)
        r=str(t)
    
    return int(r)
