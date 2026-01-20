"""
Docstring for 72.Determinants
                Efficiency: Time complexity = O(1)
                            Space complexity = O(1)
"""

# Method - 1
def det_efficient(m):
    size = len(m)
    if size == 2:
        # Formula: ad - bc
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    elif size == 3:
        # Rule of Sarrus or Cofactor Expansion
        a, b, c = m[0]
        d, e, f = m[1]
        g, h, i = m[2]
        return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    raise ValueError("Only 2x2 or 3x3 matrices supported.")

#-------------------------------------------------------------------#

# Method - 2
def s_det(m):
    if len(m) == 1: return m[0][0]
    return sum((-1)**i * m[0][i] * s_det([r[:i]+r[i+1:] for r in m[1:]]) for i in range(len(m)))

# Example: s_det([[1, 2], [3, 4]]) -> -2

#-------------------------------------------------------------------#

# Method - 3
def det_math(m):
    """Calculates determinant using formal algebraic expansion."""
    if len(m) == 2:
        # det([[a,b],[c,d]]) = ad - bc
        return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
    
    if len(m) == 3:
        # Expansion by Minors (first row)
        term1 = m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        term2 = m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        term3 = m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
        return term1 - term2 + term3

# Example: det_math([[6, 1, 1], [4, -2, 5], [2, 8, 7]]) -> -306

rows = int(input("Enter number of rows (2 or 3): "))
print("Enter elements for the matrix row by row:")
matrix = [list(map(int, input().split())) for _ in range(rows)]

try:
    print(f"\nDeterminant (Efficient): {det_efficient(matrix)}")
    print(f"Determinant (Short): {s_det(matrix)}")
    print(f"Determinant (Mathematical): {det_math(matrix)}")
except ValueError as e:
    print(f"\nError: {e}")

    