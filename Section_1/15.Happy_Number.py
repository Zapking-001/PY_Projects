"""
Docstring for 15.Happy_Number

 A Happy Number is defined as:

1. Take a positive integer n
2. Replace it with the sum of the squares of its digits.
3. Repeat the process until: You reach 1 → then n is a Happy Number.
                        Or
   you fall into a cycle that never reaches 1 → then n is Unhappy / Not a Happy Number.

Ex: n = 19                  |   n = 20
    1² + 9² = 82            |   2² + 0² = 4
    8² + 2² = 68            |   4² = 16
    6² + 8² = 100           |   1² + 6² = 37.. So on, which is never ending.
    1² + 0² + 0² = 1        |

    
                Efficiency: Time complexity = O(log n)
                            Space complexity = O(log n)

"""
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

n = int(input("Enter a number: "))

if is_happy(n):
    print(f"{n} is a happy number.")
else:
    print(f"{n} is not a happy number.")
