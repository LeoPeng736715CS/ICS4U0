"""
Variable Dictionary:
Student: Leo Peng
Course: ICS4U0
Assignment: Making Matrix's to find Magic Square 

Parameters:
n(int): input by user, represents the size of the magic square (prime number between 5 and 19)
# magic_sum(int): represents the calculated sum that each row, column, and diagonal in a magic square should equal
"""

import random
“””
Function: Finds out if the inputted number is prime

Parameters:
num(int): Number inputted by the user
“””
def prime_num(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

"""
Function: Generates the first magic square based off the user's prime number 
    
Parameters:
n(int): The size of the magic square based on input(must be prime)
 """
def first_magic_square(n):
     rows, cols = n, n
    arr = []
    r = random.randint(1, n)
    print("Random number: {}".format(r))
    for i in range(rows):
        rows = []
        for j in range (cols):
            rows.append((j-i*2+r-1)%n+1)
        arr.append(rows)
    return arr
    
"""
Function: Generates second random matrix based on transformations
    
Parameters:
n (int): The size of the magic square based on input(must be prime)
"""
def second_magic_square(n):
    rows, cols = n, n
    arr = []
    r = random.randint(0,n-1)
    print("Random number: {}".format(r))
    for i in range(rows):
        rows = []
        for j in range (cols):
            rows.append((j-i*3+r)%n*n)
        arr.append(rows)
    return arr

"""
Function: Prints a 2D matrix row by row
    
Parameters:
array: A 2D matrix
"""
def print_array(array):
    for rows in array:
        print(rows)
        
"""
Function: Adds two matrices
    
Parameters:
matrix1, matrix2: The two matrices to be added.
"""
def add_matrices(matrix1, matrix2):
    rows, cols = len(matrix1), len(matrix1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

"""
Function: Calculates the "magic sum" based off the formula: F(N)=(1+2+...+N^2)/N.
    
Parameters:
n (int): The size of the magic square.
"""
def magic_sum(n):
    
    magic_sum = n**2 * (n**2 + 1) // (n*2)
    return magic_sum

 """
 Function: Checks if all rows of the matrix sum equal to the magic sum.
    
 Parameters:
 arr(array): The matrix to check.
 magic_sum(int): The expected sum for each row.
 """
def magic_row_sum_check(arr, magic_sum):
    check = True
    rows, cols = (len(arr), len(arr[0]))
    total =  0
    row_sum = []
    for i in range (rows):
        for j in range (cols):
            total += arr[i][j]
        row_sum.append(total)
        if (total != magic_sum):
            check = False
        total = 0
    print("The row's sum is {}".format(row_sum))
    return check

"""
Function: Checks if all columns of the matrix sum equal to the magic sum.
    
Parameters:
arr (array): The matrix to check.
magic_sum (int): The expected sum for each column.
"""
def magic_column_sum_check(arr, magic_sum):
    check = True
    rows, cols = (len(arr), len(arr[0]))
    total =  0
    column_sum = []
    for i in range (cols):
        for j in range (rows):
            total += arr[j][i]
        column_sum.append(total)
        if (total != magic_sum):
            check = False
        total = 0
    print("The column's sum is {}".format(column_sum))
    return check

 """
 Function: Checks if both diagonals of the matrix sum equal to the magic sum.
    
 Parameters:
 arr (array): The matrix to check.
 magic_sum (int): The expected sum for each diagonal.
 """
def magic_diagonal_sum_checker(arr, magic_sum):
    check = True
    rows = len(arr)
    total = 0
    for i in range (rows):
        total += arr[i][i]
    print("The first diagonal's sum is {}".format(total))
    if (total != magic_sum):
        check = False
    total = 0
    for i in range(rows):
        total += arr[i][rows-i-1]
    print("The second diagonal's sum is  {}".format(total))
    if (total != magic_sum):
        check = False
    return check
    
# main workflow
# accept user input until a valid number is found
n = int(input("Put a prime number between 5 and 19: "))
while (n < 5 or n  > 19 or not prime_num(n)):
    print("The number must be a prime number between 5 and 19")
    n = int(input("Put a prime number between 5 and 19 "))
    
#generate and print 1st matrix
array1 = first_magic_square(n)
print_array(array1)
#generate and print 2nd matrix
array2 = second_magic_square(n)
print_array(array2)

#generate and print final sum magic square matrix
sum_array = add_matrices(array1, array2)
print("Sum of the Magic Squares:")
print_array(sum_array)

#generate and print magic sum based on formula
m = magic_sum(n)
print("The magic sum is {}".format(m))

#check row/column/diagonal are all match magic sum, if yes, print magic, if no print not magic
row_check = magic_row_sum_check(sum_array, m)
if (row_check): 
    print("The row of the magic square is magic")
else:
    print("The row of the magic square is not magic")
column_check = magic_column_sum_check(sum_array, m)
if (column_check): 
    print("The columns of the magic square is magic")
else:
    print("The columns of the magic square is not magic")
diagonal_check = magic_diagonal_sum_checker(sum_array, m)
if (diagonal_check):
    print("The diagonals of the magic square is magic")
else:  
    print("The diagonals of the magic square is not magic")



