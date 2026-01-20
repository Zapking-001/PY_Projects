"""
Docstring for 62.Collinearity : This program focuses on checking if ∃ a Line l ∈ ℝ | l passes through each co-ordinates (x_i,y_i)

        Formula :
                  Area =  _1_ |x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)|
                           2
        User Guide:
                  Enter the value of the co-ordinates.
        Coder Guide:
                    Give the values , If you receive the Total = 0 then, It should return Collinearity 
        Efficiency : Time complexity: O(1)  
                     Space complexity: O(1)
"""

# Method - 1

def collinearity_E():
    try:
        x1, y1 = map(float, input("Enter Point 1 (x₁ y₁): ").split())
        x2, y2 = map(float, input("Enter Point 2 (x₂ y₂): ").split())
        x3, y3 = map(float, input("Enter Point 3 (x₃ y₃): ").split())

        area_det = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)

        if area_det == 0:
            print("Output: The points are Collinear.")
        else:
            print("Output: The points are NOT Collinear.")
            
    except ValueError:
        print("Invalid input. Please enter coordinates as numbers.")

collinearity_E()

# Method - 2
def coll_shortest():
    p = [list(map(float, input(f"P{i}: ").split())) for i in range(3)]
    print("Collinear" if p[0][0]*(p[1][1]-p[2][1]) + p[1][0]*(p[2][1]-p[0][1]) + p[2][0]*(p[0][1]-p[1][1]) == 0 else "Not Collinear")

# Method - 3
def check_collinearity_mathematical():

    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    x3 = float(input("x3: "))
    y3 = float(input("y3: "))

    val1 = (y2 - y1) * (x3 - x2)
    val2 = (y3 - y2) * (x2 - x1)

    if val1 == val2:
        print("Result: Points are Collinear.")
    else:
        print("Result: Points are NOT Collinear.")