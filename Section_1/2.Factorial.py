"""
Docstring for 2.Factorial Calculation: 
                        Formula:  n! = n(n-1)(n-2)···2·1 (iterative or recursive)

                        Efficiency: Time complexity is O(n)
                                    Space complexity is O(1)
"""

def factorial(k):
    if k>0:
        prod = k*factorial(k-1)
    elif k == 0:
        prod = 1
    return prod

while True:
    n = int(input("Enter a number: "))
    try:
        print(f"{n}! = {factorial(n)}")
        break
    except:
        print("Negative numbers NOT allowed\n")
