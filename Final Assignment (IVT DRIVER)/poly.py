"""
Student: Leo Peng
Course: ICS4U0
Assignment: Final Project (The Intermediate Value Theorem (IVT))
Function: The IVT is a "brute force" algorithm to apply the same steps until there is a desirable result
"""
from polynomial import Polynomial
# Driver code to test the Polynomial class
if __name__ == "__main__":
    try:
        # Defines a polynomial with equation
        P = Polynomial([0, 0, 1, 2, 0, 3, 0, 0])
        # Print the string representation of the polynomial
        print(P)
        # Loops to evaluate the polynomial at different values of x (0 to 9)
        for i in range(10):
            print(i, P.f(i))
        print(P.get_order())
    except Exception as e:
        # This block will catch all exceptions
        print(f"An error occurred: {e}")
