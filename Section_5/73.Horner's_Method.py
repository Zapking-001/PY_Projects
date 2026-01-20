"""
Docstring for 73.Horner's_Method : Used to evaluate the Polynomial

                Efficiency: Time complexity = O(n)
                            Space complexity = O(1)
                            Where n is the number of coefficients.

"""
# Method - 1

def horner_efficient(coeffs, x):
    # coeffs: list of coefficients [an, an-1, ..., a0]
    result = 0
    for c in coeffs:
        result = result * x + c
    return result

# Example: 2x^2 + 3x + 1 at x=2 -> [2, 3, 1]
# result = 0 * 2 + 2 = 2
# result = 2 * 2 + 3 = 7
# result = 7 * 2 + 1 = 15

#-------------------------------------------------------------------#

# Method - 2
from functools import reduce
def s_horner(c, x):
    return reduce(lambda res, cur: res * x + cur, c)

# Example: s_horner([2, 3, 1], 2) -> 15

#-------------------------------------------------------------------#

# Method - 3
def horner_math(coeffs, x):
    """
    Evaluates P(x) using the nested mathematical representation.
    Coefficients are expected in order from highest degree to lowest.
    """
    def evaluate(idx):
        if idx == len(coeffs) - 1:
            return coeffs[idx]
        return coeffs[idx] + x * evaluate(idx + 1)
    
    # We reverse to start from high degree or adjust logic:
    # Let's stick to the standard high-to-low coefficient list
    res = coeffs[0]
    for i in range(1, len(coeffs)):
        res = res * x + coeffs[i]
    return res

# Example: horner_math([2, 3, 1], 2) -> 15

coeff = input("Enter coefficients (space-separated, highest degree first): ").split()
X = int(input("Enter the value of x: "))
print(horner_efficient(list(map(int, coeff)), X))
print(s_horner(list(map(int, coeff)), X))
print(horner_math(list(map(int, coeff)), X))
