"""
Docstring for 10.Sum_of_Digits : S(n) = ∑d for decimal digits dᵢ of n.

                        Efficiency: Time complexity = O(log₁₀ n)
                                    Space complexity = O(1)
"""

def Sumofdigits(k):
    sum,digits  = 0,0
    while k>0:
        digits = k%10
        sum += digits
        k //= 10
    return sum

n = int(input("Enter a valid integer: "))
print(f"The sum of digits of {n} is {Sumofdigits(n)}")
