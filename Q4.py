def intersect(A,B):
    AandB = []
    [AandB.append(x) for x in A if x in B]
    return AandB

A = [1,3,6,78,35,55]
B = [12,24,35,55,88,78,155]
print(intersect(A,B))