def add(num1, num2):
    n1=[str(num1)[i:i+1] for i in range(0,len(str(num1)),1)]
    n2=[str(num2)[i:i+1] for i in range(0,len(str(num2)),1)]
    diff=abs(len(str(num1))-len(str(num2)))

    while(diff > 0):
        if(len(n1)>len(n2)): n2.insert(0,'0')
        elif(len(n1)<len(n2)): n1.insert(0,'0')
        diff-=1
    
    return int(''.join([str(int(n1[i])+int(n2[i])) for i in range(len(n1))]))