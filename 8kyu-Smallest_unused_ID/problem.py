def next_id(arr):
    if(len(arr)==0):
        return 0

    arr.sort()
    s=[]

    for i in range(arr[len(arr)-1]+1):
        s.append(i)

    diff=set(arr).symmetric_difference(s)

    if (min(arr)==1):
        return 0;
    elif (len(diff)==0):
        return arr[len(arr)-1]+1   
    else:
        return min(diff)
