"""
Docstring for 81.Continued_Fractions

                Efficiency: Time complexity = O(depth)
                            Space complexity = O(1)
"""
# Method - 1
def evaluate_cf_efficient(coeffs):
    # coeffs: [a0, a1, a2, ..., an]
    if not coeffs: return 0
    
    # Start from the last coefficient
    result = coeffs[-1]
    
    # Iterate backwards through the remaining coefficients
    for i in range(len(coeffs) - 2, -1, -1):
        result = coeffs[i] + 1 / result
        
    return result

# Example: [1, 2] -> 1 + 1/2 = 1.5 (approximation of sqrt(2))

#-----------------------------------------------------------------------#

# Method - 2
def s_cf(c):
    return c[0] + 1 / s_cf(c[1:]) if len(c) > 1 else c[0]

# Example: s_cf([1, 2]) -> 1 + 1/2 = 1.5
#-----------------------------------------------------------------------#

# Method - 3

def cf_math(coeffs):
    """
    Computes the value using nested reciprocals truncated to desired depth.
    """
    def compute_tail(idx):
        # Base case: last coefficient
        if idx == len(coeffs) - 1:
            return coeffs[idx]
        # Recursive step: a_i + 1 / (remaining fraction)
        return coeffs[idx] + 1 / compute_tail(idx + 1)
    
    return compute_tail(0)

# Example: cf_math([1, 2]) -> 1.5

coeffs_input = input("Enter coefficients of the continued fraction (space-separated): ").split()
coeffs_list = [float(c) for c in coeffs_input]

print(f"Efficient Method: {evaluate_cf_efficient(coeffs_list):.6f}")
print(f"Short Method: {s_cf(coeffs_list):.6f}")
print(f"Mathematical Method: {cf_math(coeffs_list):.6f}")