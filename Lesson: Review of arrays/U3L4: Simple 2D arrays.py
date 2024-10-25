ar2 = [
    [3, 4, 1, 2, 6],
    [9, 2, 3, 7, 5],
    [4, 2, 1, 0, 3]
]

sums = []

for i in range(len(ar2)):
    ar3 = ar2[i] 
    row_sum = sum(ar3) 
    sums.append(row_sum)

print(sums)
