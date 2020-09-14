def ips_between(start, end):
    startIP=start.split('.')
    endIP=end.split('.')
    r=[]
    m=None

    for i in range(4):
        if (i==0): m=256**3
        elif (i==1): m=256**2
        elif (i==2): m=256
        else: m=1
        r.append((int(endIP[i])-int(startIP[i]))*m)
    
    return sum(r)
