def stem_and_leaf(data):
    d=list(map(lambda x: '0' + x if len(x)<2 else x, [str(i) for i in data]))
    s=list(set([int(i[0]) for i in d]))
    return dict(zip(s,[sorted([int(j[1]) for j in d if int(j[0])==i]) for i in s]))