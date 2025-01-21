"""
Student: Leo Peng
Course: ICS4U0
Assignment: Final Project (The Intermediate Value Theorem (IVT))
Function: The IVT is a "brute force" algorithm to apply the same steps until there is a desirable result
"""


class Polynomial:
    # Initializes the polynomial object by removing the leading zeros and calculating the degree of the polynomial
    def __init__(self, coefficients):
        """
        Variable Dictionary:
        # idx (int): An index that is used skip over leading efficients
        self.order (int): The degree of the polynomial
        """
        # Remove leading zeros
        idx = 0
        while idx < len(coefficients) and coefficients[idx] == 0:
            # Set the coefficient to exclude the leading zeroes
            idx += 1
        # Sets conditions
        self.coefficients = coefficients[idx:]
        # The order of the polynomial is the highest index of a non-zero coefficient
        self.order = len(self.coefficients) - 1 if self.coefficients else 0

    # Evaluates the polynomial at a specific value of x
    def get_order(self):
        """
        Variable Dictionary:
        self.order (int): The degree of the polynomial
        """
        return self.order

    # Returns a string representation of the polynomial
    def f(self, x):
        """
        Variable Dictionary:
        x (int/float): The input value for which the polynomial is evaluated
        idx (int): The index of the coefficient in the reversed list
        coef (int/float): The coefficient of the term in the polynomial
        """

        # The sum of coef * (x ** idx) for each coefficient and its corresponding exponent
        return sum(coef * (x ** idx) for idx, coef in enumerate(reversed(self.coefficients)))

    # Represents the string representation of the polynomial
    def __str__(self):
        # List to hold the terms of the polynomial
        terms = []
        for idx, coef in enumerate(reversed(self.coefficients)):
            # Builds a string representation for each turn
            term = f"{coef}x^{idx}"
            terms.append(term)
        # result string to be returned
        result = ""
        # Reverses the terms so that they are ordered from highest to lowest
        for idx, t in enumerate(reversed(terms)):
            # check term's sign is "+" or "-"
            if t[0] == "-":
                # if "-", format it properly
                result += " - " + t[1:]
            else:
                # if first order, just append it
                if idx == 0:
                    result += t
                # others format it properly with " + "
                else:
                    result += " + " + t
        return result
