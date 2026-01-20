"""
Docstring for 5.Armstrong Number: It is a special case of perfect number.
        It is a number if sum of it's digits raised to power of the number of digits equals the number;
        Ex_1: 153 = 1^3 + 5^3 + 3^3 ; where { 1,5,3 } are the digits of 153 & 153 is a three digit number hence, it is raised to the power of 3.

        Efficiency: Time complexity is O(log₁₀ n)
                    Space complexity is O(log₁₀ n)

"""

def is_Armstrong(k):
    if k <= 0:
        return False
    num_digits = len(str(k))
    sum_of_digits = sum(int(digit) ** num_digits for digit in str(k))
    return sum_of_digits == k

n = int(input("Enter the number: "))

if is_Armstrong(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
