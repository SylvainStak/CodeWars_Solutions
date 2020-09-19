def beggars(values, n):
    r=[0]*n
    if (n==0): return []
    for i in range(len(values)):
        r[i%n]+=values[i]
    return r