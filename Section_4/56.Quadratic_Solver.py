"""
Docstring for 56.Quadratic_Solver

            Efficiency : Time complexity: O(1)
                         Space complexity: O(1)
"""

# Method - 1

import math as m
while True:
    try:
        c1,c2,c3 = map(float,input("Enter the coefficients of Quadratic Equation: ").split())
        def roots(a,b,c):
            delta = (b**2) - (4*(a*c))
            if delta >= 0:
                x1 = (-b - m.sqrt(delta))/(2*a)
                x2 = (-b + m.sqrt(delta))/(2*a)
                return x1,x2
            else:
                return "No Real Roots"

        print(f"Roots: {roots(c1,c2,c3)}")
        break
    except:
        print("Non Zero coefficients pls")

# Method - 2

c1,c2,c3 = map(float,input("Enter the coefficients of Quadratic Equation: ").split())
def root_finder(a,b,c):
    if a ==0 and b==0 and c==0:
        return "∀ x ∈ ℝ ∃ a Solution always."
    else:
        if a == 0 and b !=0 and c != 0:
            return  f"x = {-c/b}"
        elif a == 0 and b == 0 and c != 0:
            return "No Real Roots"
        else:
            pass
    d = b**2 - 4*a*c
    if d >= 0:
        x1 = (-b + (d)**0.5) / (2*a)
        x2 = (-b - (d)**0.5) / (2*a)
        return x1,x2
    elif d<0:
        return f"\n{-b} + i{round((abs(d))**0.5,2)}\n─────────────\n\t{2*a}" f"\n\n{-b} - i{(round((abs(d))**0.5,2))}\n─────────────\n     {2*a}" 
print(f"Roots: {root_finder(c1,c2,c3)}")


# Method - 3  For best presentation.

import math
import cmath

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            return ("all_real" if c == 0 else "no_solution", [])
        return ("linear", [-c / b])

    delta = b*b - 4*a*c
    if delta >= 0:
        sqrt_delta = math.sqrt(delta)

        x1 = (-b - math.copysign(sqrt_delta, b)) / (2*a)
        x2 = c / (a * x1) if x1 != 0 else (-b + sqrt_delta) / (2*a)
        return ("real", [x1, x2])
    else:
        sqrt_delta = cmath.sqrt(delta)  # complex
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        return ("complex", [x1, x2])

a,b,c = map(float,input("Enter the coefficients of Quadratic Equation: ").split())
result_type, roots = solve_quadratic(a, b, c)

if result_type == "real":
    print(f"Real roots: {roots[0]:.2f}, {roots[1]:.2f}")
elif result_type == "complex":
    print(f"Complex roots: {roots[0]:.2f}, {roots[1]:.2f}")
elif result_type == "linear":
    print(f"Linear equation, one root: {roots[0]:.2f}")
elif result_type == "all_real":
    print("All real numbers are solutions.")
else: # no_solution
    print("No solution. No Real Roots")