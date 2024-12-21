"""
Student: Leo Peng
Course: ICS4U0
Assignment: A3 Polygon Object (Part 2)
"""
# Driver for the polygon class
from poly import Polygon

# input: S is a point in the format "(x,y)" (type str)
# output: a tuple or list indicating a point (x, y) where x, y are int or float
def getNumeric(S : str):
    """
    Variable dictionary:
    S (str): The string representation of the point in the format "(x, y)".
    x, y (float): The numerical coordinates extracted from the string.
    """
    try:
        x, y = map(float, S.replace("(","").replace(")","").split(","))
        return x, y
    except ValueError as e:
        print(f"Error: {e}. Input string was: '{S}'")
        return S.replace("(","").replace(")","").split(",")

def main():
    try:
        # Opens the file "a2.txt" for reading
        with open("a2.txt", "r") as file:
            for line in file:
                try:
                    # Creates a new polygon object for each line of points
                    myPoly = Polygon()
 #                  print(f"Reading line: {line.strip()}")  # Debugging step
                    points = line.replace(" ","").strip().split("),(")
                    points[0] = points[0].replace("(", "")
                    points[-1] = points[-1].replace(")", "")
                    # For each point in the list, get the numeric coordinates and add them to the polygon
                    for point in points:
                        x, y = getNumeric(point)
                        # Add the point to the polygon
                        myPoly.add_point(x, y)

                    # Prints the string representation of the polygon
                    print(myPoly)
                    # Prints the perimeter and area of the polygon
                    print("Perimeter:", myPoly.perimeter())
                    print("Area:", myPoly.area())

                    # Checks if the polygon is regular and prints out the amount of sides it has
                    if myPoly.is_regular():
                        print(f"This is a regular polygon with {myPoly.sidesCount} sides")
                    else:
                        print(f"This is an irregular polygon with {myPoly.sidesCount} sides")
                    # Plots the polygon using turtle graphics
                    myPoly.plot()
                    # Prints a blank line for better readability
                    print()
                # Catches any error in the value expressions
                except ValueError as e:
                    print(f"ValueError: {e}")
                    continue
            # Finishes the turtle graphics session after processing all lines
            import turtle
            turtle.done()
    # Handles exception where the file "a2.txt" is not found
    except FileNotFoundError:
        print("File not found. Please make sure 'a2.txt' is in the same directory as your script.")
        return
    # Handles any general ValueError exceptions
    except ValueError as e:
        print(f"ValueError: {e}")
        return

if __name__ == "__main__":
    main()
