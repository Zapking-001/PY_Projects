"""
Docstring for 77.P__&__C

                Efficiency: Time complexity = O(r)
                            Space complexity = O(1)

"""

# Method - 1
def combinations_efficient(n, r):
    if r < 0 or r > n: return 0
    if r == 0 or r == n: return 1
    if r > n // 2: r = n - r # Use symmetry property nCr = nC(n-r)
    
    num = 1
    for i in range(r):
        num = num * (n - i) // (i + 1)
    return num

def permutations_efficient(n, r):
    if r < 0 or r > n: return 0
    res = 1
    for i in range(n, n - r, -1):
        res *= i
    return res

#---------------------------------------------------------------------------#

# Method - 2
import math
def s_comb_perm(n, r):
    return math.comb(n, r), math.perm(n, r)

# Example: s_comb_perm(5, 2) -> (10, 20)

#---------------------------------------------------------------------------#

# Method - 3

def factorial_math(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def comb_perm_math(n, r):
    # Strictly following the formulas from the PDF
    n_fact = factorial_math(n)
    r_fact = factorial_math(r)
    nmr_fact = factorial_math(n - r)
    
    nPr = n_fact // nmr_fact
    nCr = n_fact // (r_fact * nmr_fact)
    
    return nCr, nPr

# Example: comb_perm_math(5, 2) -> (10, 20)

n = int(input("Enter n: "))
r = int(input("Enter r: "))

print(f"Combinations (Efficient): {combinations_efficient(n, r)}")
print(f"Permutations (Efficient): {permutations_efficient(n, r)}")

s_comb, s_perm = s_comb_perm(n, r)
print(f"Combinations (Short): {s_comb}")
print(f"Permutations (Short): {s_perm}")

math_comb, math_perm = comb_perm_math(n, r)
print(f"Combinations (Mathematical): {math_comb}")
print(f"Permutations (Mathematical): {math_perm}")