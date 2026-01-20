"""
Docstring for 69.LCM_in_List

                Efficiency: Time complexity = O(n x log(max_val))
                            Space complexity = O(log(max_val))
                            where max_val is the largest number in the list.

"""
# Method - 1
from math import gcd
from functools import reduce

def lcm_efficient(numbers):
    def lcm(a, b):
        if a == 0 or b == 0: return 0
        return abs(a * b) // gcd(a, b)
    return reduce(lcm, numbers)

# Example: lcm_efficient([12, 18, 20]) -> 180

#-----------------------------------------------------#

# Method - 2

import math
s_lcm = lambda l: math.lcm(*l)

# Example: s_lcm([12, 18, 20]) -> 180

#-----------------------------------------------------#

# Method - 3
def get_prime_factors(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1: factors[n] = factors.get(n, 0) + 1
    return factors

def lcm_math(numbers):
    max_factors = {}
    for n in numbers:
        f = get_prime_factors(n)
        for p, count in f.items():
            max_factors[p] = max(max_factors.get(p, 0), count)
    
    res = 1
    for p, count in max_factors.items():
        res *= (p ** count)
    return res

# Example: lcm_math([12, 18, 20]) -> 180

numbers_input = input("Enter numbers separated by spaces: ").split()
numbers_list = [int(num) for num in numbers_input]

print(f"LCM (Efficient): {lcm_efficient(numbers_list)}")
print(f"LCM (Short): {s_lcm(numbers_list)}")
print(f"LCM (Mathematical): {lcm_math(numbers_list)}")

#-----------------------------------------------------#