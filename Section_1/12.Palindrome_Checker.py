"""
Docstring for 12.Palindrome : IF a number or any is reversed and results equal
        Ex: RADAR = RADAR ; CIVIC = CIVIC
            BEFORE != EROFEB

        Efficiency: Time complexity is O(log₁₀ n)
                    Space complexity is O(1)
"""
n = input("Enter the number: ")

if n == n[::-1]:
    print(f"{n} is a Palindrome")
else:
    print(f"{n} is not a Palindrome")

#For a Mathematical approach ; 

def is_palindromic(n):
    original = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10 
    return original == rev

if is_palindromic(int(input("Enter the number: "))):
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")