"""
Student: Leo Peng
Course: ICS4U0
Assignment: A3 Polygon Object (Part 2)
"""
import math
# Class that represents a point in 2D space
class Point:
    """
    Variable dictionary:
    x (float): The x coordinate of the point
    y (float): The y coordinate of the point
    """
    def __init__(self, x: float=None, y: float=None):
        # Default is None due to creation of a Head Node for linked lists
        self.__x = x
        self.__y = y
        # Points to the next point in the list
        self.next = None

    def valid(self):
        """
        Variable dictionary:
        None (boolean): True if the point is valid, otherwise False.
        """
        # A validator is needed mostly for when we go to the end of the file, but
        # also to assure us that the point is properly formatted with either
        # ints or floats.

        # return invalid if either coordinate is None
        if self.__x is None or self.__y is None:
            return False

        # return invalid if either coordinates are not an int or a float
        if not isinstance(self.__x, (int, float)) or not isinstance(self.__y, (int, float)):
            return False
        # return valid
        return True

    def get_x(self):
        # Returns the x-coordinate of the point
        return self.__x

    def get_y(self):
        # Returns the y-coordinate of the point
        return self.__y

    def distance(self, p2):
        # Calculates the distance between this point and another point
        return math.sqrt((self.__x - p2.get_x()) ** 2 + (self.__y - p2.get_y()) ** 2)

    def __str__(self):
        # Returns the point as a string with proper format
        return f"({self.__x}, {self.__y})"

class Vertex(Point):
    def __init__(self, x, y):
        # Calls the constructor of the Point class
        super().__init__(x, y)

class Polygon:
    """
    Variable dictionary:
    sidesCount (int): The number of sides in the polygon.
    verticesCount (int): The number of vertices in the polygon.
    head (Point or None): Points to the first vertex (head node) in the linked list of points.
    """

    # Set basic properties to default values
    def __init__(self):
        # init the number of sides in the polygon
        self.sidesCount = 0
        # init the number of vertices in the polygon
        self.verticesCount = 0
        # init the head point to none in the polygon's linked list
        self.__head = None

    # Adds a new point to the polygon's vertex list
    def add_point(self, x: float, y: float):
        """
        Variable dictionary:
        x (float): The x-coordinate of the new point to be added to the polygon.
        y (float): The y-coordinate of the new point to be added to the polygon.
        point (Point): An instance of the Point class representing the new point being added.
        current (Point): A temporary reference used to traverse the existing linked list of points,
        starting from the head, to find where to insert the new point.
        """
        # create a point object V
        point = Point(x, y)
        if point.valid():
            # Counts the vertices as it continuously goes up
            self.verticesCount += 1
            # Counts the sides as it continuously goes up
            self.sidesCount += 1
            # If it is the first point, create the object with variable V make head.next point to V
            if not self.__head:
                self.__head = point
                self.__head.next = self.__head
            # if it is any other point, append the new point to the circular linked list which point back to head point
            else:
                current = self.__head
                while current.next != self.__head:
                    current = current.next
                current.next = point
                point.next = self.__head
        else:
            print(f"Invalid point {x}, {y}")

    def __str__(self):
        """
        Variable dictionary:
        output (str): A string that accumulates the string representation of the points in the polygon.
        current (Point): A pointer used to traverse through the linked list of points.
        """
        # Use a traversal to generate the entire set of points separated by "->" as string
        # use point's __str__ function to build.
        output = ""
        if self.__head:
            current = self.__head
            while True:
                output += current.__str__() + " -> "
                current = current.next
                # End of list, which then goes back to the head
                if current == self.__head:
                    break
        return output + self.__head.__str__()

    def is_regular(self):
        """
        Variable dictionary:
        n (int): The number of vertices in the polygon.
        side_length (float): The length of the first side, used to compare other sides.
        current (point): A pointer used to traverse the linked list to check side lengths and angles.
        regular_interior_angle (float): The expected interior angle of a regular polygon with n sides.
        angle (float): The calculated angle for each vertex.
        """
        n = self.verticesCount
        # Polygon needs to have at least 3 sides
        if n < 3:
            return False
        # Compares all side length's to the first side's length
        side_length = self.__head.distance(self.__head.next)
        current = self.__head.next
        while True:
            # If any of the sides are not the same length as the first, it is not a regular polygon
            if current.distance(current.next) != side_length:
                return False
            current = current.next
            # End of list, which makes it go back to the head
            if current == self.__head:
                break
        #caculate regular n sides polygon angle
        regular_interior_angle = (n - 2) * 180 / n
        current = self.__head
        while True:
            # Calculates the angle at the current vertex
            angle = self.calculate_angle(current)
            # If angle does not equal regular angle or larger than 180 degrees, it is not a regular polygon
            if angle != regular_interior_angle or angle > 180:
                return False
            current = current.next
            # End of list, makes it go back to head
            if current.next == self.__head:
                break
        return True

    def perimeter(self):
        """
        Variable dictionary:
        n (int): The number of vertices in the polygon.
        side_length (float): The length of one side of the polygon.
        perimeter (float): The total perimeter of the polygon.
        current (Point): A pointer used to traverse through the linked list and accumulate side lengths.
        """
        if self.is_regular():
            n = self.verticesCount
            #calcuate the first side length
            side_length = self.__head.distance(self.__head.next)
            # If it is a regular polygon, multiply the side length by the number of sides
            return n * side_length
        else:
            perimeter = 0
            current = self.__head
            while True:
                # Adds the distance between consecutive points
                perimeter += current.distance(current.next)
                current = current.next
                # End of list, goes back to head
                if current == self.__head:
                    break
            return perimeter

    def area(self):
        """
        Variable dictionary:
        n (int): The number of vertices in the polygon.
        side_length (float): The length of one side of the polygon.
        area (float): The calculated area of the polygon.
        current (Point): A pointer used to traverse through the linked list to calculate the area.
        """
        if self.is_regular():
            n = self.verticesCount
            side_length = self.__head.distance(self.__head.next)
            # I used math.pi because I had to change 180 degrees to 3.14 radians (pi radians)
            return (n * side_length ** 2) / (4 * math.tan(math.pi / n))
        else:
            area = 0
            current = self.__head
            while True:
                #use formula for each p1,p2 point x, y coordinates to calculate
                x1, y1 = current.get_x(), current.get_y()
                x2, y2 = current.next.get_x(), current.next.get_y()
                area += x1 * y2 - x2 * y1
                current = current.next
                # End of list, which makes it go back to the head
                if current == self.__head:
                    break
            return abs(area) / 2

    def plot(self):
        """
        Variable dictionary:
        t (Turtle): The turtle object used to plot the polygon.
        current (Point): A pointer used to traverse the linked list and plot each point.
        None (returns None): Displays the polygon using turtle graphics.
        """
        import turtle
        t = turtle.Turtle()
        t.penup()
        # Starts at the first point of the turtle
        t.goto(self.__head.get_x(), self.__head.get_y())
        t.pendown()
        current = self.__head
        while True:
            # Moves the turtle to each point
            t.goto(current.get_x(), current.get_y())
            current = current.next
            if current == self.__head:
                break
        # Completes the shape
        t.goto(current.get_x(), current.get_y())

    def calculate_angle(self, node):
        """
        Variable dictionary:
        A (Point): The first point of the vertex angle (the point before the current vertex).
        B (Point): The current vertex (the point whose angle is being calculated).
        C (Point): The third point of the vertex angle (the point after the current vertex).
        BA (tuple): The vector from B to A.
        BC (tuple): The vector from B to C.
        dot_product (float): The dot product of vectors BA and BC.
        magnitude_BA (float): The magnitude (length) of vector BA.
        magnitude_BC (float): The magnitude (length) of vector BC.
        cosine_angle (float): The cosine of the angle at B.
        angle (float): The angle at vertex B, calculated in degrees.
        """
        A = node
        B = node.next
        C = node.next.next

        # Create vectors from B to A (BA) and from B to C (BC)
        BA = (A.get_x() - B.get_x(), A.get_y() - B.get_y())
        BC = (C.get_x() - B.get_x(), C.get_y() - B.get_y())

        # Calculates the dot product of BA and BC
        dot_product = BA[0] * BC[0] + BA[1] * BC[1]
        # Calculate the magnitudes (lengths) of the vectors
        magnitude_BA = A.distance(B)
        magnitude_BC = B.distance(C)

        # Uses the cosine rule to calculate the cosine of the angle
        cosine_angle = dot_product / (magnitude_BA * magnitude_BC)
        angle = math.acos(cosine_angle)

        # Calculate the angle in radians and convert to degrees
        return math.degrees(angle)
