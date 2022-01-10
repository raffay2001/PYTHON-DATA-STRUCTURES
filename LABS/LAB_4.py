def matMul(A, B):
    # A is a M x P Matrix 
    # B is a P x N Matrix 
    # The Product C will be M x N Matrix 

    if len(A[0]) == len(B):
        C = []
        for row in range(len(A)):
            lst = []
            for col in range(len(B[0])):
                lst.append(0)
            C.append(lst)
        
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] += A[i][k] * B[k][j]
        return C
    else:
        return f"Invalid Dimensions"

A = [
    [2, 3, 4],
    [2, 3, 6],
]
# A --> 2 x 3 
# B --> 3 x 2 
B = [
    [1,2],
    [4,5],
    [7,8]
]

C = [
    [1,2],
    [3,4]
]
# C --> 2 x 2
# D --> 2 x 2

D = [
    [1,2],
    [3,4],
]

print('Result of A and B: ', matMul(A, B))
print('Result of C and D: ', matMul(C, D))