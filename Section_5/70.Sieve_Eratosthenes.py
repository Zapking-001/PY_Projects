"""
Docstring for 70.Sieve_Eratosthenes

                Efficiency: Time complexity = O(n log log n)
                            Space complexity = O(n)
"""

# Method - 1
def sieve_efficient(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]

# Example: sieve_efficient(20) -> [2, 3, 5, 7, 11, 13, 17, 19]

#-----------------------------------------------------#

# Method - 2
def sieve_short(n):
    s = set(range(2, n + 1))
    for i in range(2, int(n**0.5) + 1):
        if i in s: s -= set(range(i*i, n + 1, i))
    return sorted(list(s))

# Example: sieve_short(20) -> [2, 3, 5, 7, 11, 13, 17, 19]

#-----------------------------------------------------#

# Method - 3
def sieve_math(n):
    # Strictly following the marking of multiples of each prime starting from 2
    # to generate primes <= N.
    nums = list(range(n + 1))
    for p in range(2, int(n**0.5) + 1):
        if nums[p] != 0:
            # Mark multiples by setting them to zero
            for i in range(p * p, n + 1, p):
                nums[i] = 0
    return [p for p in nums if p > 1]

# Example: sieve_math(20) -> [2, 3, 5, 7, 11, 13, 17, 19]

n = int(input("Enter a number: "))
print(f"Primes up to {n} (Efficient): {sieve_efficient(n)}")
print(f"Primes up to {n} (Short): {sieve_short(n)}")
print(f"Primes up to {n} (Mathematical): {sieve_math(n)}")

#-----------------------------------------------------#