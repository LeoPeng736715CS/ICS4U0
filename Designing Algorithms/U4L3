import turtle

# File I/O
fileName = "smiley_emoji_mod"
lines = []

try:
	fh = open(fileName + ".xpm")
	eof = False
	while not eof:
		lines.append(fh.readline())
		eof = lines[len(lines) - 1] == ""
	
	fh.close()
except OSError as oserr:
	print("OSError:", oserr)
except EOFError as eoferr:
	print("EOFError:", eoferr)

# Removes all quotation marks and commas in a string
def getCleanLine(clutteredString):
	return clutteredString.strip().replace(",", "").replace("\"", "")

# Get metadata (cols, rows, colours)
# Get the cleaned up version of the first line
metaDataStr = getCleanLine(lines[0])
# Split metaDataStr and convert all elements to integers
cols, rows, numColours = [int(n) for n in metaDataStr.split()]

# Get colours
colourData = {}
for c in range(1, numColours + 1):
	tempColourData = getCleanLine(lines[c]).split()
	
	symbol = tempColourData[0]
	# If the symbol is a lone slash, that means it was meant to be a space
	if symbol == "\\":
		symbol = " "
	colourData[symbol] = tempColourData[2]
	
# Get image
imageMap = []
for p in range(numColours + 1, len(lines)):
	imageMap.append(getCleanLine(lines[p]))

# Turtle
def drawDot(turtleObj, diameter, colour):
	turtleObj.pendown()
	turtleObj.dot(diameter, colour)
	turtleObj.penup()

t = turtle.Turtle()
turtle.tracer(0, 0)
# turtle.hideturtle()
turtle.step = 4

# Move to initial position
turtle.forward(-cols/2 * turtle.step)
turtle.left(90)
turtle.forward(rows/2 * turtle.step)
turtle.right(90)

for row in range(rows):
	for col in range(cols):
		currPixel = imageMap[row][col]
		currColour = colourData[currPixel]
		drawDot(turtle, turtle.step, currColour)
		turtle.forward(turtle.step)
	
	turtle.right(90)
	turtle.forward(turtle.step)
	turtle.left(90)
	turtle.forward(-cols*turtle.step)
	print(turtle.pos())
# drawDot(turtle, 4, "red")

turtle.done()
