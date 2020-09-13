def number(lines):
    r=[]
    if(len(lines)==0):
        return []
    else:
        for i in range(1,len(lines)+1):
            r.append(str(i)+': '+lines[i-1])   

    return r
