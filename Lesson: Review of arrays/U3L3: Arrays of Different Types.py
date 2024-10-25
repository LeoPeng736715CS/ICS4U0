items = ["Apples", "Bananas", "Cherries", "Dosa"]
sizes = []

for i in range(len(items)):
    sizeI = len(items[i])
    sizes.append(sizeI)

for i in range(len(sizes)):
    print("%d %s" % (sizes[i], items[i]))

for i in range(len(items)):
    comparison = sizes[i] == len(items[i])
    print(comparison)
