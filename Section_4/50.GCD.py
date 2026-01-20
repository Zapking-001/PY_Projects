"""
Docstring for 50.GCD

        Efficiency : Time complexity: O(log(min(a,b)))
                     Space complexity: O(log(min(a,b))

"""

a,b = map(int,input("Enter the two numbers: ").split())

# Method - 1
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(f"GCD: {gcd(a, b)}")

# Method - 2 
import math
print(f"GCD: {math.gcd(a, b)}")

# Method - 3
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)
print(f"GCD: {gcd_recursive(a, b)}")
