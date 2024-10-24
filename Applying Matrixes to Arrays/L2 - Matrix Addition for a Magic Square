def addM(M1, M2):
    if len(M1) != len(M2) or len(M1[0]) != len(M2[0]):
        raise ValueError("Matrices must be of the same dimension to add")
    return [[M1[i][j] + M2[i][j] for j in range(len(M1[0]))] for i in range(len(M1))]

def isMagic(M, magic_sum=65):
    
    if n == 0 or len(M[0]) != n:  
        return False

    for i in range(n):
        if sum(M[i]) != magic_sum or sum(row[i] for row in M) != magic_sum:
            return False
    
    if sum(M[i][i] for i in range(n)) != magic_sum or sum(M[i][n - i - 1] for i in range(n)) != magic_sum:
        return False

    return True

def make5x5(M, shift):
    if len(M) != 5:
        raise ValueError("Input array must be of length 5 to form a 5x5 matrix")
    
    matrix_5x5 = [M]
    
    for i in range(1, 5):
        shifted_row = [(val + shift * i) for val in M]
        matrix_5x5.append(shifted_row)
    
    return matrix_5x5

a1 = [5, 1, 4, 2, 3]    
b1 = [15, 20, 0, 10, 5]

A = make5x5(a1, 2)
B = make5x5(b1, 3)

sum_matrix = addM(A, B)

print("Sum Matrix is Magic (sums to 65):", isMagic(sum_matrix))

print("\nMatrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nSum of Matrix A and Matrix B:")
for row in sum_matrix:
    print(row)
