"""
Docstring for 4.Perfect Number Checker: if Sum of it's Factors equals to the number itself.
        Ex_1: 6 = 1 + 2 + 3 ; where { 1,2,3 } are the factors of 6.
        Ex_2: 28 = 1 + 2 + 4 + 7 + 14 ; where { 1,2,4,7,14 } are the factors of 28.
        Ex_3: 496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248 ; where { 1,2,4,8,16,31,62,124,248 } are the factors of 496.

        Efficiency: Time complexity is O(√n)
                    Space complexity is O(1)
"""

def is_perfect(k):
    if k <= 0:
        return False
    divisors_sum = sum(i for i in range(1, k) if k % i == 0)
    return divisors_sum == k

n = int(input("Enter the number: "))

if is_perfect(n):
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")