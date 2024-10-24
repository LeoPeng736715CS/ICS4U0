def addM(M1, M2):
    if len(M1) != len(M2) or len(M1[0]) != len(M2[0]):
        raise ValueError("Matrices must be of the same dimension to add")
    return [[M1[i][j] + M2[i][j] for j in range(len(M1[0]))] for i in range(len(M1))]

def isMagic(M):
    n = len(M)
    magic_sum = sum(M[0]) 
    
      
def addM(M1, M2):
    if len(M1) != len(M2) or len(M1[0]) != len(M2[0]):
        raise ValueError("Matrices must be of the same dimension to add")
    return [[M1[i][j] + M2[i][j] for j in range(len(M1[0]))] for i in range(len(M1))]

def isMagic(M):
    n = len(M)
    magic_sum = sum(M[0])  

    for i in range(n):
        if sum(M[i]) != magic_sum or sum(row[i] for row in M) != magic_sum:
            return False
    
    if sum(M[i][i] for i in range(n)) != magic_sum or sum(M[i][n - i - 1] for i in range(n)) != magic_sum:
        return False
    
    return True

def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M))]

def rotate(M):
    return [[M[len(M) - j - 1][i] for j in range(len(M))] for i in range(len(M))]

def reflect(M):
    return [row[::-1] for row in M]

m1 = [2, 7, 6]
m2 = [9, 5, 1]
m3 = [4, 3, 8]
M = [m1, m2, m3]


print("Original Matrix is Magic:", isMagic(M))

M_self_add = addM(M, M)
print("Matrix + Itself is Magic:", isMagic(M_self_add))

M_duplicate = [row[:] for row in M]
M_duplicate_add = addM(M, M_duplicate)
print("Matrix + Duplicate is Magic:", isMagic(M_duplicate_add))

M_rotated = rotate(M)
M_rotated_add = addM(M, M_rotated)
print("Matrix + Rotated is Magic:", isMagic(M_rotated_add))

M_reflected = reflect(M)
M_reflected_add = addM(M, M_reflected)
print("Matrix + Reflected is Magic:", isMagic(M_reflected_add))

M_transposed = transpose(M)
M_transposed_add = addM(M, M_transposed)
print("Matrix + Transposed is Magic:", isMagic(M_transposed_add))

print("\nOriginal Matrix:")
for row in M:
    print(row)

print("\nMatrix + Itself:")
for row in M_self_add:
    print(row)

print("\nMatrix + Rotated:")
for row in M_rotated_add:
    print(row)

print("\nMatrix + Reflected:")
for row in M_reflected_add:
    print(row)

print("\nMatrix + Transposed:")
for row in M_transposed_add:
    print(row)
