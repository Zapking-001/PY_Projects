"""
Docstring for 61.Slope_of_Line

            Efficiency : Time complexity: O(1)
                         Space complexity: O(1)
"""

# Method - 1
def slope_E():
    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        if x1 == x2:
            raise ValueError()
        else:
            slope = (y2 - y1) / (x2 - x1)
            print(f"Output: {slope}")
    except ValueError:
        print("Slope: Not defined / ∞")

slope_E()

# Method - 2
def slope_s():
    x1, y1, x2, y2 = map(float, input("Enter x1 y1 x2 y2: ").split())
    print((y2 - y1) / (x2 - x1) if x1 != x2 else "Undefined")

slope_s()

# Method - 3
def slope_m():
    # Manual Input
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    # Difference in coordinates
    dy = y2 - y1
    dx = x2 - x1

    # Manual check for zero denominator
    if dx == 0:
        print("The line is vertical; slope is undefined.")
    else:
        # Simple division from basic arithmetic
        m = dy / dx
        print("Slope:", m)

slope_m()