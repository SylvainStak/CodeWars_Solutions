def dative(word):
    fV=['e','é','i','í','ö','ő','ü','ű']
    bV=['a','á','o','ó','u','ú']

    for i in reversed(word):
        if (i in bV):
            return word+'nak'
        elif (i in fV):
            return word+'nek'
