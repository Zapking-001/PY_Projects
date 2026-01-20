"""
Docstring for Section_1.11.Reversing_num
            
            Efficiency: Time complexity is O(log₁₀ n)
                        Space complexity is O(1)

"""
n = input("Enter a number ≥ 10:  ")
print(f"Reversed Number = {n[::-1]}")

# The above is the two line code of reversing the digits.

print(f"Reversed Number = {input("Enter a number ≥ 10:  ")[::-1]}")
# The above is the single line code of reversing the digits.


def reverse_number(n): 
    rev = 0 
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev

num = int(input("Enter a number ≥ 10:  "))
print(f"Reversed Number = {reverse_number(num)}")

# The above is the right and the way used by Mathematician + Coder. 