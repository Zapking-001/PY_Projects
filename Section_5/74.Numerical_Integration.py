"""
Docstring for 74.Numerical_Integration

        Formula ∫ₐᵇf(x)dx ≈ h/2 [ f(x0) + f(xn) + ∑f(xi) ]

                Efficiency: Time complexity = O(n)
                            Space complexity = O(1)


"""
# Method - 1
def trapezoidal_efficient(f, a, b, n):
    h = (b - a) / n
    # The first and last terms are added once, middle terms twice
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + i * h)
    return integral * h

# Example: Integrate x^2 from 0 to 1 with 100 intervals
# trapezoidal_efficient(lambda x: x**2, 0, 1, 100)

#-------------------------------------------------------------------

# Method - 2
def s_trap(f, a, b, n):
    h = (b - a) / n
    return (h / 2) * (f(a) + f(b) + 2 * sum(f(a + i * h) for i in range(1, n)))

#-------------------------------------------------------------------

# Method - 3
def trapezoidal_math(f, a, b, n):
    h = (b - a) / n
    x_values = [a + i * h for i in range(n + 1)]
    
    # Calculate each term based on the formal summation
    terms = []
    for i in range(len(x_values)):
        val = f(x_values[i])
        if i == 0 or i == n:
            terms.append(val)      # f(x0) and f(xn)
        else:
            terms.append(2 * val)  # 2 * f(xi)
            
    return (h / 2) * sum(terms)

# Example: trapezoidal_math(lambda x: x**2, 0, 1, 100)

# Test the functions
# Define a function to integrate, e.g., f(x) = x^2
def my_function(x):
    return x**2

# Define integration limits and number of intervals
a = 0
b = 1
n = 100

print(f"Efficient Method: {trapezoidal_efficient(my_function, a, b, n)}")
print(f"Short Method: {s_trap(my_function, a, b, n)}")
print(f"Mathematical Method: {trapezoidal_math(my_function, a, b, n)}")