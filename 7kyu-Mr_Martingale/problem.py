def martingale(bank, outcomes): 
    s=100
    for i in outcomes:
        if(i==1):
            bank+=s
            s=100
        else:
            bank-=s
            s=s*2
    return bank