"""
Docstring for 51.LCM

        Efficiency : Time complexity: O(log(min(a,b))
                     Space complexity: O(log(min(a,b))
"""
a,b = map(int,input("Enter the two numbers: ").split())

# Method - 1
def lcm(a, b):
    import math
    return abs(a*b) // math.gcd(a, b)

# Method - 2
lcm = lambda a,b: abs(a*b)//__import__('math').gcd(a,b)
print(f"LCM: {lcm(a, b)}")

# Method - 3
def lcm_recursive(a, b):
    # lcm(a,b) = |a*b| / gcd(a,b)
    def gcd(x, y):
        return x if y == 0 else gcd(y, x % y)
    return abs(a*b) // gcd(a, b)
print(f"LCM: {lcm_recursive(a, b)}")