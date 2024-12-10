"""
Student: Leo Peng
Course: ICS4U0
Assignment: A2 Polygon Object (Part 1)
Function: To create a polygon object that displays the connected points as a closed loop
"""

# driver for the polygon class
from poly import Polygon

# input: S is a point in the format "(x,y)" (type str)
# output: a tuple or list indicating a point (x, y) where x, y are int or float
# Converts a string representing a point in the format "(x, y)" into a tuple (x, y)
def getNumeric(S : str):
    """
    Variable dictionary:
    S (str): A string representing a point in the format "(x,y)".
    x (float): The x-coordinate of the point, parsed as a float.
    y (float): The y-coordinate of the point, parsed as a float.
    polydata (str): A single line of text from the file, containing the points.
    """
    try:
        x, y = map(float, S.replace("(","").replace(")","").split(","))
        return x, y
    except ValueError as e:
        print(f"Error: {e}. Input string was: '{S}'")
        return S.replace("(","").replace(")","").split(",")

try:
    # this is the name of the data file to open
    fh = open("a2.txt", "r")

    polydata = fh.readline().strip()
    # make an array of points (str)
    points = polydata.replace(" ","").strip().split("),(")
    # declare a polygon
    polygon = Polygon()
    # loop through the points array and turn them into numbers for the polynomial object
        # generate an x, y pair (numerical not str) from getNumeric
        # add to the polynomial (call add_point())
    for point in points:
        x, y = getNumeric(point)
        polygon.add_point(x, y)

    # this should print the entire linked list of points as string
    print(polygon)

    # e (Exception): Stores details of a file not found error.
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
    # e (Exception): Stores details of any unexpected error during execution.
except Exception as e:
    print(f"unexpected error occurred: {e}")
