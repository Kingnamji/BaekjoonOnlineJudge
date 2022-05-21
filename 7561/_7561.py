# 7561 크래머의 공식
import sys
from copy import deepcopy

# 3by3 matrix's determinant
def det3(A):
    det = ( A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1]) - 
            A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0]) + 
            A[0][2]*(A[1][0]*A[2][1]- A[1][1]*A[2][0]) )

    return det

# Crammer's rule for 3by3 matrix
def crammer(A, b):
    det_An = [] # A_n's determinant list
    det_A = det3(A)
    
    # Calculate A_n's determinant
    for i in range(3):
        An = deepcopy(A)
        An[0][i] = b[0]
        An[1][i] = b[1]
        An[2][i] = b[2]
        
        det_An.append(det3(An))

    if det_A: # case : A's determinant is not zero
        print(*det_An, det_A)
        print("Unique solution:", end=' ')
        for i in range(3):
            x_i = det_An[i] / det_A
            if -0.0005 < x_i and x_i < 0.0005:
                print("0.000", end=' ')
            else:
                print(f"{x_i:.3f}", end=' ')

    else: # case : A's determinant is zero
        print(*det_An, det_A)
        print("No unique solution", end='')

    print("\n")


# Solution
T = int(input()) # Num of test case

for _ in range(T):
    A = [] # A : matrix
    b = [] # b : column vector

    # 3 row 
    for _ in range(3):
        row = list(map(int, sys.stdin.readline().split()))
        A.append(row[:3])
        b.append(row[-1])

    crammer(A, b)
