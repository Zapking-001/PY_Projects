"""
Docstring for 8.Conversion of Decimal to Binary, we can use the direct in-built function and we can String slice it to show it in the desired format.

               Efficiency: Time complexity = O(log₂ n)
                           Space complexity = O(log₂ n)
"""
n = int(input("Enter the Decimal number: "))

Decimal_to_Binary = bin(n)[2:]

print(f"Binary({n}) = {Decimal_to_Binary}")