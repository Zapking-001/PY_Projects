"""
Docstring for 78.Cube_root_Finder

                Efficiency: Time complexity = O(iterations)
                            Space complexity = O(1)

"""

# Method - 1

def solve_cubic_efficient(a, b, c, d, x0, tol=1e-7, max_iter=100):
    x = x0
    for _ in range(max_iter):
        # f(x) = ax^3 + bx^2 + cx + d
        fx = a*x**3 + b*x**2 + c*x + d
        # f'(x) = 3ax^2 + 2bx + c
        dfx = 3*a*x**2 + 2*b*x + c
        
        if abs(dfx) < 1e-12: break # Avoid division by zero
        
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

#-------------------------------------------------------------------#

# Method - 2
def s_newton(a, b, c, d, x):
    f = lambda x: a*x**3 + b*x**2 + c*x + d
    df = lambda x: 3*a*x**2 + 2*b*x + c
    return x if abs(f(x)) < 1e-7 else s_newton(a, b, c, d, x - f(x)/df(x))

#-------------------------------------------------------------------#

# Method - 3
def f(x, coeffs):
    a, b, c, d = coeffs
    return a*x**3 + b*x**2 + c*x + d

def df(x, coeffs):
    a, b, c, d = coeffs
    return 3*a*x**2 + 2*b*x + c

def solve_cubic_math(coeffs, x0, iterations=10):
    # Strictly follows the formula x_k+1 = x_k - f(x_k)/f'(x_k)
    x = x0
    for k in range(iterations):
        x = x - f(x, coeffs) / df(x, coeffs)
    return x

# Example: x^3 - 6x^2 + 11x - 6 = 0, roots are 1, 2, 3
# solve_cubic_efficient(1, -6, 11, -6, 0.5) -> 1.0
# solve_cubic_efficient(1, -6, 11, -6, 1.5) -> 2.0
# solve_cubic_efficient(1, -6, 11, -6, 2.5) -> 3.0

# s_newton(1, -6, 11, -6, 0.5) -> 1.0
# s_newton(1, -6, 11, -6, 1.5) -> 2.0
# s_newton(1, -6, 11, -6, 2.5) -> 3.0

# solve_cubic_math((1, -6, 11, -6), 0.5) -> 1.0
# solve_cubic_math((1, -6, 11, -6), 1.5) -> 2.0
# solve_cubic_math((1, -6, 11, -6), 2.5) -> 3.0