"""
Docstring for 3.Fibonacci Sequence Generator: F0 = 0, F1 = 1, 
                        Formula: Fn = Fn-1 + Fn-2 for n ≥ 2.

                        Efficiency: Time complexity is O(n)
                                    Space complexity is O(1)
"""

while True:
    try:
        def fibonacci(n):
            a, b = 0, 1
            if n>=2:
                for _ in range(n):
                    print(a, end=" ")
                    a, b = b, a + b
            else:
                raise ValueError()

        # Example: print first 10 Fibonacci numbers
        fibonacci(int(input("Enter the Range: ")))
        break
    except:
        print("Only Positive inputs are allowed")
