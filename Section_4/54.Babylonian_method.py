"""
Docstring for 54.Babylonian_method: The Square root approximation method.
            Goal: Approximate √S for a positive number S
            Method : 
                    > Start with an initial guess x0 (often S/2 or 1).
                    > Iteratively refine using:x(k+1)=1/2(xk+S/xk)
                    > Stop when the difference between successive guesses is smaller than a tolerance (e.g., 10¯⁶)
                    
            Efficiency : Time complexity: O(log(1/tolerance)) == O(log(precision))
                         Space complexity: O(1)


"""

# Method - 1
n = float(input("Enter the number: "))
def sqrt_babylonian(S, tolerance=1e-6):
    if S < 0:
        raise ValueError("Cannot compute square root of negative number")
    if S == 0:
        return 0
    
    x = S / 2 if S > 1 else 1  # initial guess
    while True:
        next_x = 0.5 * (x + S / x)
        if abs(next_x - x) < tolerance:
            return next_x
        x = next_x


print(f"√{n} ≈ {sqrt_babylonian(n):.3f}")

# Method - 2
import math as m
print(f"≈{m.sqrt(float(input("Enter the number: "))):.3f}")