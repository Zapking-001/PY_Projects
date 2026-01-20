"""
Docstring for 7.Leap Year: By Gregorian rule, A year is a leap year if it is divisible by 4 and not by 100, unless it is also divisible by 400.

                Efficiency: Time complexity is O(1)
                            Space complexity is O(1)
"""
def is_Leapyear(k):
    if k <= 0:
        return False
    
    if (k % 4 == 0 and k % 100 != 0) or (k % 400 == 0):
        return True
    else:
        return False

n = int(input("Enter the Year: "))

if is_Leapyear(n):
    print(f"{n} is a Leap Year.")
else:
    print(f"{n} is not a Leap Year.")