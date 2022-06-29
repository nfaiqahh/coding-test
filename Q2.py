def uni(a):
    unique = []
    [unique.append(x) for x in a if x not in unique]

uni(['b', 'a', 'c', 'b', 'f'])