"""
Docstring for 76.Linear_eqn's

                Efficiency: Time complexity = O(1)
                            Space complexity = O(1)
"""
# Method - 1
def det2x2(m):
    return m[0][0]*m[1][1] - m[0][1]*m[1][0]

def solve_2x2(A, B):
    # A is [[a, b], [c, d]], B is [e, f]
    main_det = det2x2(A)
    if main_det == 0: return None # No unique solution
    
    det_x = det2x2([[B[0], A[0][1]], [B[1], A[1][1]]])
    det_y = det2x2([[A[0][0], B[0]], [A[1][0], B[1]]])
    
    return [det_x / main_det, det_y / main_det]

# Example: 2x + 3y = 8, 4x - y = 2
# solve_2x2([[2, 3], [4, -1]], [8, 2]) -> [1.0, 2.0]

#-------------------------------------------------------------------#

# Method - 2
def s_solve(a, b, c, d, e, f):
    det = a*d - b*c
    return (e*d - b*f)/det, (a*f - e*c)/det if det != 0 else None

# Example: s_solve(2, 3, 4, -1, 8, 2) -> [1.0, 2.0]
#-------------------------------------------------------------------#

# Method - 3

def get_det3x3(m):
    a, b, c = m[0]; d, e, f = m[1]; g, h, i = m[2]
    return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

def solve_3x3_math(A, B):
    D = get_det3x3(A)
    if D == 0: return "No unique solution"
    
    # Construct matrices Ax, Ay, Az by replacing columns with vector B
    Ax = [[B[i], A[i][1], A[i][2]] for i in range(3)]
    Ay = [[A[i][0], B[i], A[i][2]] for i in range(3)]
    Az = [[A[i][0], A[i][1], B[i]] for i in range(3)]
    
    return [get_det3x3(Ax)/D, get_det3x3(Ay)/D, get_det3x3(Az)/D]

# Example: x + 2y + 3z = 6, 2x + y - z = 2, x + y + z = 3
# A = [[1, 2, 3], [2, 1, -1], [1, 1, 1]], B = [6, 2, 3]
# solve_3x3_math(A, B) -> [1.0, 1.0, 1.0]

print("--- 2x2 Linear Equations ---")
a1, b1, c1 = map(float, input("Enter coefficients for eq 1 (a b c for ax + by = c): ").split())
a2, b2, c2 = map(float, input("Enter coefficients for eq 2 (a b c for ax + by = c): ").split())

A_2x2 = [[a1, b1], [a2, b2]]
B_2x2 = [c1, c2]

solution_efficient_2x2 = solve_2x2(A_2x2, B_2x2)
if solution_efficient_2x2:
    print(f"Efficient Method (2x2): x = {solution_efficient_2x2[0]:.2f}, y = {solution_efficient_2x2[1]:.2f}")
else:
    print("Efficient Method (2x2): No unique solution.")

solution_short_2x2 = s_solve(a1, b1, a2, b2, c1, c2)
if solution_short_2x2:
    print(f"Short Method (2x2): x = {solution_short_2x2[0]:.2f}, y = {solution_short_2x2[1]:.2f}")
else:
    print("Short Method (2x2): No unique solution.")

print("\n--- 3x3 Linear Equations ---")
a11, a12, a13, b1 = map(float, input("Enter coefficients for eq 1 (a b c d for ax + by + cz = d): ").split())
a21, a22, a23, b2 = map(float, input("Enter coefficients for eq 2 (a b c d for ax + by + cz = d): ").split())
a31, a32, a33, b3 = map(float, input("Enter coefficients for eq 3 (a b c d for ax + by + cz = d): ").split())