def solve(n): 
    p=[]
    i=1

    while len(''.join(p))<n:
        m=''
        for j in range(i):
            m+=str(j+1)
        p.append(m)
        i+=1

    return int(''.join(p)[n-1])