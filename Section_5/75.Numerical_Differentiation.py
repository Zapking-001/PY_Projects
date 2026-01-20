"""
Docstring for 75.Numerical_Differentiation
                Efficiency: Time complexity = O(1)
                            Space complexity = O(1)

"""

# Method - 1
def diff_efficient(f, x, h=1e-5):
    # Central difference formula for better accuracy
    return (f(x + h) - f(x - h)) / (2 * h)

# Example: Derivative of x^2 at x=3
# diff_efficient(lambda x: x**2, 3) -> ~6.0

#-------------------------------------------------------------------#

# Method - 2
def s_diff(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

# Example: s_diff(lambda x: x**2, 3) -> ~6.00001

#-------------------------------------------------------------------#

# Method - 3

def diff_math(f, x, h=1e-5, method='central'):
    """
    Computes the derivative based on formal difference quotients.
    """
    if method == 'forward':
        # Forward difference formula: O(h) accuracy
        numerator = f(x + h) - f(x)
        denominator = h
    else:
        # Central difference formula: O(h^2) accuracy
        numerator = f(x + h) - f(x - h)
        denominator = 2 * h
        
    return numerator / denominator

# Example: diff_math(lambda x: x**2, 3, method='central') -> ~6.00

# Test the functions
def my_function(x):
    return x**2

x_val = 3
h_val = 1e-2

print(f"Efficient Method: {diff_efficient(my_function, x_val, h_val)}")
print(f"Short Method: {s_diff(my_function, x_val, h_val)}")
print(f"Mathematical Method (Central): {diff_math(my_function, x_val, h_val, 'central')}")
print(f"Mathematical Method (Forward): {diff_math(my_function, x_val, h_val, 'forward')}")