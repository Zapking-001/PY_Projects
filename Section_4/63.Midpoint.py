"""
Docstring for 63.Midpoint Segment Calculator: Helps to determine the Midpoint for Given two points


            Efficiency : Time complexity: O(1)
                         Space complexity: O(1)

"""

# Method - 1
def midpoint_e():
    try:
        x1, y1 = map(float, input("Enter Point 1 (x₁ y₁): ").split())
        x2, y2 = map(float, input("Enter Point 2 (x₂ y₂): ").split())

        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
    
        print(f"(Xₘ,Yₘ) = {mid_x,mid_y}")
    except ValueError:
        print("Invalid input. Please enter coordinates as numbers.")

midpoint_e()

# Method - 2 
def mid_S():
    p1 = list(map(float, input("P1: ").split())); p2 = list(map(float, input("P2: ").split()))
    print(f"Midpoint: ({(p1[0]+p2[0])/2}, {(p1[1]+p2[1])/2})")
mid_S()

# Method - 3
def midpoint_m():
    x1 = float(input("x₁: "))
    y1 = float(input("y₁: "))
    x2 = float(input("x₂: "))
    y2 = float(input("y₂: "))

    sum_x = x1 + x2
    sum_y = y1 + y2
    
    mid_x = sum_x / 2
    mid_y = sum_y / 2
    
    print(f"(Xₘ,Yₘ) = {mid_x,mid_y}")


midpoint_m()