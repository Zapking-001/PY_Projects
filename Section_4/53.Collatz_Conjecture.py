"""
Docstring for 53.Collatz_Conjecture : 

        Goal: Compute the number of steps needed for a given 'n' to reach 1 under the Collatz rules.
        Rules:
              > If n is even , n → n/2
              > If n is odd , n → 3n + 1
              > Until n == 1

            Efficiency : Time complexity: O(steps)
                         Space complexity: O(1)

"""
n = int(input("Enter a number: "))

# Method - 1
def collatz_steps(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be a positive integer")
    steps = 0
    while n != 1:
        if n & 1 == 0:     # even check via bit
            n >>= 1        # n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

print(f"Steps: {collatz_steps(n)}")

# Method - 2
def collatz_steps(n):
    s = 0
    while n > 1:
        n = (n // 2) if n % 2 == 0 else (3*n + 1)
        s += 1
    return s

print(f"Steps: {collatz_steps(n)}")


# Method - 3 
def collatz_steps_recursive(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + collatz_steps_recursive(n // 2)
    return 1 + collatz_steps_recursive(3 * n + 1)

print(f"Steps: {collatz_steps_recursive(n)}")