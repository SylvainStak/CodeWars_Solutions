import math

def get_turkish_number(num):
    n=[0,1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90]
    w=['sıfır','bir','iki','üç','dört','beş','altı','yedi','sekiz','dokuz','on','yirmi','otuz','kırk','elli','altmış','yetmiş','seksen','doksan']
    
    for i in range(len(n)):
        if(num==n[i]):
            return w[i]

    d=math.floor((num%100)/10)*10
    u=num%10
    r=''

    for i in range(len(n)):
        if(d==n[i]):
            r+=w[i]

    for i in range(len(n)):
        if(u==n[i]):
            r+=' '+w[i]

    return r
