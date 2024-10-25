def linsearch(arr, target):
    found = False  
    for index in range(len(arr)):
        if arr[index] == target:
            found = True
            print(f"Value {target} found at index: {index}")
    if not found:
        print(f"Value {target} not found in the array.")

myArr = [20, 20, 24, 27, 39, 40, 43, 46, 50, 
         60, 60, 62, 71, 74, 76, 86, 86, 87, 97, 97]

targets = [20, 25, 60, 74, 97]

for target in targets:
    linsearch(myArr, target)
