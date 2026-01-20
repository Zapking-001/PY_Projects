"""
Docstring for 66.Prime_Factorization
"""
# Method - 1
def factorize_efficient(n):
    factors = {}
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors[d] = factors.get(d, 0) + 1
            temp //= d
        d += 1
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    return factors

# Example: 360 -> {2: 3, 3: 2, 5: 1}

#-----------------------------------------------------#

# Method - 2
def f(n, i=2):
    return [] if n < 2 else ([i] + f(n//i, i) if n%i == 0 else f(n, i+1))

# Example: f(360) -> [2, 2, 2, 3, 3, 5]

#-----------------------------------------------------#


# Method - 3

def factorize_math(n: int) -> str:
    """Returns the LaTeX formatted prime factorization."""
    res = []
    d = 2
    temp = n
    while d * d <= temp:
        count = 0
        while temp % d == 0:
            count += 1
            temp //= d
        if count > 0:
            res.append(f"{d}^{{{count}}}" if count > 1 else f"{d}")
        d += 1
    if temp > 1:
        res.append(f"{temp}")
    return f"{n} = " + " \\cdot ".join(res)

# Example output: "360 = 2^{3} \cdot 3^{2} \cdot 5"

n = int(input("Enter a number: "))
print(factorize_efficient(n))
print(f(n))
print(factorize_math(n))

#-----------------------------------------------------#