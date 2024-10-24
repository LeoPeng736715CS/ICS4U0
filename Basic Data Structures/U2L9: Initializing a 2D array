Magic3 = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

def is_magic_square(square):
    n = len(square)
    target_sum = sum(square[0])
    
    for i in range(n):
        if sum(square[i]) != target_sum or sum(row[i] for row in square) != target_sum:
            return False
    
    if sum(square[i][i] for i in range(n)) != target_sum or sum(square[i][n - i - 1] for i in range(n)) != target_sum:
        return False
    
    print(f"All rows, columns, and diagonals sum to {target_sum}.")
    return True

def add_scalar(square, value):
    """Add a scalar to each element in the square."""
    return [[cell + value for cell in row] for row in square]

def subtract_scalar(square, value):
    """Subtract a scalar from each element in the square."""
    return [[cell - value for cell in row] for row in square]

def multiply_scalar(square, value):
    """Multiply each element in the square by a scalar."""
    return [[cell * value for cell in row] for row in square]

print("Part a: Checking initial magic square.")
is_magic_square(Magic3)

scalar_add = 3
new_square_add = add_scalar(Magic3, scalar_add)
new_magic_number_add = 15 + 3 * 3 
print("\nPart b: Adding scalar", scalar_add)
is_magic_square(new_square_add)
print("New magic number:", new_magic_number_add)

scalar_subtract = 1
new_square_subtract = subtract_scalar(Magic3, scalar_subtract)
new_magic_number_subtract = 15 - 1 * 3
print("\nPart c: Subtracting scalar", scalar_subtract)
is_magic_square(new_square_subtract)
print("New magic number:", new_magic_number_subtract)

scalar_multiply = 2
new_square_multiply = multiply_scalar(Magic3, scalar_multiply)
new_magic_number_multiply = 15 * scalar_multiply
print("\nPart d: Multiplying by scalar", scalar_multiply)
is_magic_square(new_square_multiply)
print("New magic number:", new_magic_number_multiply)
