"""
Student: Leo Peng
Course: ICS4U0
Assignment: Final Project (The Intermediate Value Theorem (IVT))
Function: The IVT is a "brute force" algorithm to apply the same steps until there is a desirable result
"""


class IVT:
    # Initializes an instance of the IVT
    def __init__(self, polynomial):
        # Polynomial that will be used for fighting the zero
        self.polynomial = polynomial

    # Uses the IVT to find a zero of the polynomial
    def findZero(self, x1, x2):
        """
        Variable Dictionary:
        x1 (float): The lower bound of the interval.
        x2 (float): The upper bound of the interval.
        f_x1 (float): The value of the polynomial at x1.
        f_x2 (float): The value of the polynomial at x2.
        x0 (float): The midpoint of the interval [x1, x2] used for binary search.
        f_x0 (float): The value of the polynomial at x0.
        """
        # Checks if the bounds are the same (not valid for the method)
        if x1 == x2:
            return "x1 and x2 must be different"

        # Evaluates the polynomial at the bounds of the interval
        f_x1 = self.polynomial.f(x1)
        f_x2 = self.polynomial.f(x2)

        # If the function values at the bound have the same signs, there is not a root in the interval
        if f_x1 * f_x2 > 0:
            return "No zero found in the interval"

        # Uses binary search to find a zero with the interval
        while abs(x2 - x1) > 0.0004:
            # Midpoint of the current interval
            x0 = (x1 + x2) / 2
            f_x0 = self.polynomial.f(x0)

            # If the polynomial value at x0 is near enough to zero, it returns x0 as the root
            if abs(f_x0) < 0.0004:
                return x0
            # Narrows down the interval
            if f_x0 * f_x2 < 0:
                # Root between x0 and x2
                x1 = x0
            else:
                # Root between x1 and x0
                x2 = x0

        # Returns midpoint of the first interval as the approximate root
        return (x1 + x2) / 2
