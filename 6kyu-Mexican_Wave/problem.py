def wave(people):
    r=[]
    for i in range(len(people)):
        if(people[i]!=' '):
            w=list(people)
            w[i]=list(people)[i].upper()
            r.append(''.join(w))
    return r