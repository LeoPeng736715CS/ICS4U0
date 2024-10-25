little =   {"hairy":"rat", "clever":"bat", "slow":"cod", "bare":"ant", "quick":"cat"}
midsized = {"hairy":"ewe", "clever":"fox", "slow":"pig", "bare":"eel", "quick":"doe"}
large =    {"hairy":"gnu", "clever":"ape", "slow":"cow", "bare":"elephant", "quick":"nag"}

animals = {"little": little, "midsized": midsized, "large": large}

# Get the inner keys from one of the sub-hashes (e.g., little)
innerKeys = animals["little"]

# Nested loop to access and describe each animal
for size in animals:
    for trait in innerKeys:
        animal = animals[size][trait]  # Accessing the animal by size and trait
        print(f"The {animal} is {size} and {trait}")
