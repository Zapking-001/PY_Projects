"""
Docstring for 52.Exponentiation :  Fast exponentiation via binary exponentiation: Exponentiation in O(logy).

            Efficiency : Time complexity: O(logy)
                         Space complexity: O(logy)

"""
x,y = map(int, input("Enter the value of x and y for Xʸ format: ").split())

# Method - 1
def power(x, y):
    result = 1
    while y > 0:
        if y % 2 == 1:   # if y is odd
            result *= x
        x *= x           # square the base
        y //= 2          # halve the exponent
    return result

print("Xʸ = ", power(x, y))
    
# Method - 2
print(f"Xʸ = {int(input("X = "))**int(input("Y = "))}")

# Method - 3
def power_recursive(x, y):
    if y == 0:
        return 1
    half = power_recursive(x, y // 2)
    return half * half if y % 2 == 0 else x * half * half

print("Xʸ = ", power_recursive(x, y))


