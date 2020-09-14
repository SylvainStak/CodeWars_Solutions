def narcissistic(value):
    sumArr=[]

    for i in str(value):
        sumArr.append(int(i)**len(str(value)))

    if (sum(sumArr)==value):
        return True
    else: 
        return False
