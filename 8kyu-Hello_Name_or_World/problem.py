def hello(name='Hello, World!'):
    if name is hello.__defaults__[0] or name is '': return hello.__defaults__[0]
    else: 
        n=[i.lower() for i in name]
        n[0]=n[0].upper()
        n=''.join(n)
    return 'Hello, '+n+'!'
