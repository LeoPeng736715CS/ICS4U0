"""
Student: Leo Peng
Course: ICS4U0
Assignment: A2 Polygon Object (Part 1)
Function: To create a polygon object that displays the connected points as a closed loop
"""

class Point:
    # Initializes the x and y coordinates of the point
    def __init__(self, x: float=None, y: float=None):
        """
        Variable dictionary:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
        self.__x (float): Private storage for the x-coordinate.
        self.__y (float): Private storage for the y-coordinate.
        self.next (Point): Points to the next Point in the linked list.
        """
        # Default is None due to creation of a Head Node for linked lists
        self.__x = x
        self.__y = y
        self.next = None

    # Validates that the point is valid with proper x and y coordinates values
    def valid(self):
        """
        Variable Dictionary:
        val (bool): Tracks if the point is valid.
        """
        # A validator is needed mostly for when we go to the end of the file, but
        # also to assure us that the point is properly formatted with either
        # ints or floats.
        val = False
        if self.__x is None or self.__y is None:
            return val

        if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
            return val

        val = True
        return val

    # Returns the point as a string in the format "(x, y)".
    def __str__(self):
        # point (x, y) expressed this way as string
        # as in: (4, 5)
        return f"({self.__x}, {self.__y})"

class Polygon:
    # Initialize a polygon with default properties.
    def __init__(self):
        """
        Variable Dictionary:
        self.__sides (int): The number of sides in the polygon.
        self.__vertices (int): The number of vertices in the polygon.
        self.__head (Point or None): Reference to the first point in the circular linked list.
        """
        # Set basic properties to default values
        self.__sides = 0
        self.__vertices = 0
        self.__head = None # a null point with a null Next field

    # Adds a point to the polygon as part of a circular linked list.
    def add_point(self, x: float, y: float):
        """
        Variable Dictionary:
        - x (float): The x-coordinate of the new point.
        - y (float): The y-coordinate of the new point.
        - point (Point): A new Point object created with the given x and y.
        - current (Point): Used to traverse the linked list to find the last point.
        """
        # initialize a point object V
        # if it is the first point, create the object with variable V make head.next point to V
        # if it is any other point, V.next points to it, and V traverses to that point
        # count the vertices as you go
        point = Point(x, y)
        if point.valid():
            self.__vertices += 1
            self.__sides += 1
            # if it is the first point, create the object with variable V make head.next point to V
            if not self.__head:
                self.__head = point
                self.__head.next = self.__head
            # if it is any other point, V.next points to it, and V traverses to that point
            else:
                current = self.__head
                while current.next != self.__head:
                    current = current.next
                current.next = point
                point.next = self.__head
        else:
            print(f"Invalid point {x}, {y}")

    # Goes through the circular linked list and return all points to the string
    def __str__(self):
        """
        Variable Dictionary:
        current (Point): Used to traverse the linked list of points.
        """
        # Use a traversal to generate the entire set of points separated by "->" as string
        nodes = []
        if self.__head:
            current = self.__head
            while True:
                nodes.append(current.__str__())
                current = current.next
                if current == self.__head:
                    break
        return " -> ".join(nodes)
