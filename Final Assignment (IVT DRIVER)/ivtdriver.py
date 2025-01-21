"""
Student: Leo Peng
Course: ICS4U0
Assignment: Final Project (The Intermediate Value Theorem (IVT))
Function: The IVT is a "brute force" algorithm to apply the same steps until there is a desirable result
"""
from polynomial import Polynomial
from ivt import IVT

try:
    # Defines a polynomial
    P = Polynomial([1, 0, -2])  # Example polynomial f(x) = x^2 - 2

    # Create IVT instance
    ivt = IVT(P)

    # Find the zero of the polynomial
    x1 = 0
    x2 = 2
    # Calls the findZero method to find the root in the interval
    zero = ivt.findZero(x1, x2)
    print(f"The zero of the interval ({x1},{x2}) the polynomial ({P.__str__()}) is approximately {zero}")
    # Example with different polynomials
    P = Polynomial([1, -6, 11, -6])
    poly = IVT(P)
    # Adjust x1 and x2 as needed
    x1 = 1.0
    x2 = 3.0
    zero1 = poly.findZero(x1, x2)
    print(f"The zero of the interval ({x1},{x2}) the polynomial ({P.__str__()}) is approximately {zero1}")
except Exception as e:
    # This block will catch all exceptions
    print(f"An error occurred: {e}")
