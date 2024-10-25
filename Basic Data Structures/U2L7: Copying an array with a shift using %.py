a = [7, 1, 3, 5, 2, 4, 6]

n = len(a)

b = [0] * n  


for i in range(n):
    b[i] = a[(i - 2) % n]  

print("Before (Original array a):", a)
print("After (Shifted array b):", b)
