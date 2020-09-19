def anagrams(word, words):
    return [i for i in words if ''.join(sorted(i))==''.join(sorted(word))]
