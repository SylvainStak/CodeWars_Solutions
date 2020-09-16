def name_value(l):
    return [sum(ord(j)-96 for j in l[i])*(i+1) for i in range(len(l))]
