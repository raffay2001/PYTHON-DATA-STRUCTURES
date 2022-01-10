# Algorithm A5.1 
A = [[1,0,0],[2,3,0],[4,5,6]]
# here A is a lower triangular matrix of order 3 x 3.
def storeTriangular(array):
    U = []
    for i in range(len(A)):
        for j in range(len(A)):
            if j <= i:
                U.append(A[i][j])
    return U
# print(storeTriangular(A))

from math import *

from scipy.sparse.csr import csr_matrix
# Algorithm A5.2
U = [1,1,2,1,2,3]
def retrieveTriangular(U):
    a = 1
    b = 1
    c = -2*len(U) 
    d = b**2-4*a*c
    x1 = (-b+sqrt(d))/(2*a)
    x2 = (-b-sqrt(d))/(2*a)
    if x1.real > x2.real:
        c = int(x1.real)
    else:
        c = int(x2.real)
    A = []
    count = 0
    for i in range(c):
        lst = []
        for j in range(c):
            if j <= i:
                lst.append(U[count])
                count += 1
            else:
                lst.append(0)
        A.append(lst)
    return A
# print(retrieveTriangular(U))

# part c 
# Algo to store the non-zero values of a Tridiagonal Matrix B in a linear array U.
def storeTriDiagonal(array):
    U = []
    for i in range(len(array)):
        for j in range(len(array)):
            # checking for the first row 
            if i == 0 and j in [0,1]:
                U.append(array[i][j])
            # checking for the last row
            elif i == len(array)-1 and j in [len(array)-1, len(array)-2]:
                U.append(array[i][j])
            # for all the middle rows 
            else:
                if j >= i-1 and j <= i+1:
                    U.append(array[i][j])
    return U
    
B = [
    [1,2,0,0,0,0],
    [3,4,5,0,0,0],
    [0,6,7,8,0,0],
    [0,0,9,10,11,0],
    [0,0,0,12,13,14],
    [0,0,0,0,15,16],
]
# print(storeTriDiagonal(B))
                
# Algo to retrieve the non-zero values from a linear array U and place them ina triadiagonal matrix B 
def retrieveTriDiagonal(U):
    B = []
    count = 0
    # for n 
    n = int((len(U)+2)/3)
    for i in range(n):
        lst = []
        for j in range(n):
            if i == 0 and j in [0,1]:
                lst.append(U[count])
                count += 1
            elif i == n-1 and j in [n-1, n-2]:
                lst.append(U[count])
                count += 1
            elif j >= i-1 and j <= i+1:
                lst.append(U[count])
                count += 1
            else:
                lst.append(0)
        B.append(lst)
    return B
U = [5, -7, 1, 4, 3, 9, -3, 6, 2, 4]
# print(retrieveTriDiagonal(U))


from scipy.sparse import *
import numpy as np

mat = [
    [1, 23, 0, 0, 0],
    [1, 2, 8, 0 , 0],
    [0, 0, 20, 0, 0],
]

dense_arr = np.array(mat)
crr = csr_matrix(dense_arr)
dense_arr2 = csr_matrix.todense(crr)

print(crr)
print(dense_arr2)
print(dense_arr)