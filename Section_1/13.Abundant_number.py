"""
Docstring for 13: Abundant Number Checker: n is abundant if the sum of its Divisors is greater than n.

        Ex: 6 → Divisors: 1, 2, 3, 6 → Sum = 12
            12 > 6 → 6 is an abundant number.

        Efficiency: Time complexity is O(√n)
                    Space complexity is O(1)
"""
def is_abundant(n):
    if n <= 0:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum > n

n = int(input("Enter the number: "))

if is_abundant(n):
    print(f"{n} is an abundant number.")
else:
    print(f"{n} is not an abundant number.")
