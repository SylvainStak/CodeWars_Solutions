def rot13(message):
    n=[]
    for i in message:
        m=97 if ord(i) in range(97,122) else 65 if ord(i) in range(65,90) else False
        r=(((ord(i)-m)+13)%26)+m if m!=False else ord(i)
        n.append(chr(r))            
        
    return ''.join(n)
