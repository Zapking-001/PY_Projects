"""
Docstring for 67.AP_gener

            Efficiency : Time complexity: O(n)
                         Space complexity: O(1)

"""
# Method - 1
def ap_efficient(a, d, n):
    """
    a: first term, d: common difference, n: number of terms
    """
    current = a
    for _ in range(n):
        yield current
        current += d

# Example: list(ap_efficient(5, 3, 5)) -> [5, 8, 11, 14, 17]

#-----------------------------------------------------#

# Method - 2
def s_ap(a, d, n):
    return list(range(a, a + n * d, d))

# Example: s_ap(5, 3, 5) -> [5, 8, 11, 14, 17]

#-----------------------------------------------------#

# Method - 3

def ap_math(a, d, n):
    # Using the closed-form formula for every index k
    return [a + (k * d) for k in range(n)]

# Example: ap_math(10, 5, 4) -> [10, 15, 20, 25]

#-----------------------------------------------------#

s = input("Enter the first term (a), common difference (d), and number of terms (n): ").split()
a = int(s[0])
d = int(s[1])
n = int(s[2])

print(list(ap_efficient(a, d, n)))
print(s_ap(a, d, n))
print(ap_math(a, d, n))

#-----------------------------------------------------#