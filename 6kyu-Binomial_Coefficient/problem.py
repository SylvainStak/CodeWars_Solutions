import math

def choose(n,k):
    if (k<n):
        return int(math.factorial(n)//(math.factorial(k)*math.factorial(n-k)))
    elif (n<k):
        return 0
    else:
        return 1
