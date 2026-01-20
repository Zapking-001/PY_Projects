"""
Docstring for 17.Palindrome_for_String : This program represent the Palindrome for a String, it can be two or more words.

            Efficiency: Time complexity is O(n)
                        Space complexity is O(1)
"""
import re

# n = re.sub(r"\s+", "", input("Enter a String: "))     OR
n = input("Enter a String: ").replace(" ","")
if n == n[::-1]:
    print(f"{n} is a Palindrome")
else:
    print(f"{n} is not a Palindrome")
