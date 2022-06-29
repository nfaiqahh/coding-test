def printlist(A,B):
    for x in range(len(A)):
        sentence = str(A[x]) + ' is ' + str(B[0][x]) + ' years old and his height is ' + str(B[1][x]) + 'ft.'
        print(sentence)

A = ['Ali','Hamza','Usman']
B = [[ 23, 29, 32], [ 5.8, 5.9, 6.1]]
printlist(A,B)