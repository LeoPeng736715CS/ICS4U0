progname = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras semper."

space_count = 0

for char in progname:
    if char == ' ':
        space_count += 1

print(f"There are {space_count} spaces in the text.")
