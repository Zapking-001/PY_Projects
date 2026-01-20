"""
Docstring for 80.Dist_POL

                Efficiency: Time complexity = O(1)
                            Space complexity = O(1)
"""

# Method - 1
import math

def dist_efficient(A, B, C, x0, y0):
    # Shortest distance from (x0, y0) to Ax + By + C = 0
    # Numerator: |Ax0 + By0 + C|
    # Denominator: sqrt(A^2 + B^2)
    return abs(A * x0 + B * y0 + C) / math.sqrt(A**2 + B**2)

# Example: Point (1, 2) to line 3x + 4y - 6 = 0
# dist_efficient(3, 4, -6, 1, 2) -> 1.0

#-------------------------------------------------------------------------#

# Method - 2

import math
s_dist = lambda A, B, C, x, y: abs(A*x + B*y + C) / (A**2 + B**2)**0.5

# Example: s_dist(3, 4, -6, 1, 2) -> 1.0

#-------------------------------------------------------------------------#

# Method - 3
import math

def dist_math(line_coeffs, point):
    """
    Computes distance using the formal geometric formula.
    line_coeffs: (A, B, C) for Ax + By + C = 0
    point: (x0, y0)
    """
    A, B, C = line_coeffs
    x0, y0 = point
    
    numerator = abs(A * x0 + B * y0 + C)
    denominator = math.sqrt(A**2 + B**2)
    
    return numerator / denominator

# Example Usage
A_coeff = float(input("Enter coefficient A for the line Ax + By + C = 0: "))
B_coeff = float(input("Enter coefficient B for the line Ax + By + C = 0: "))
C_coeff = float(input("Enter coefficient C for the line Ax + By + C = 0: "))
x_point = float(input("Enter x-coordinate for the point (x0, y0): "))
y_point = float(input("Enter y-coordinate for the point (x0, y0): "))

# Check for valid line coefficients (A and B cannot both be zero)
if A_coeff == 0 and B_coeff == 0:
    print("Error: Coefficients A and B cannot both be zero for a valid line.")
else:
    efficient_result = dist_efficient(A_coeff, B_coeff, C_coeff, x_point, y_point)
    print(f"\nEfficient Method: Distance = {efficient_result:.4f}")

    short_result = s_dist(A_coeff, B_coeff, C_coeff, x_point, y_point)
    print(f"Short Method: Distance = {short_result:.4f}")

    math_result = dist_math((A_coeff, B_coeff, C_coeff), (x_point, y_point))
    print(f"Mathematical Method: Distance = {math_result:.4f}")

