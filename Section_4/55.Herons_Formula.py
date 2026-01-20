"""
Docstring for 55.Herons_Formula

            Efficiency : Time complexity: O(1)
                         Space complexity: O(1)
"""

# Method - 1
import math as m
def area_herons(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a: 
        raise ValueError("Invalid triangle sides: triangle inequality violated.")
    s = (a+b+c)/2.0
    area1 = m.sqrt(s*(s-a)*(s-b)*(s-c))
    area1 = round(area1,2)
       
    # Guard against tiny negative due to floating error
    return (max(area1, 0.0))

while True:
    try:
        a,b,c = map(float,input("Enter the three sides of Triangle: ").split())
        print(f"Area: {area_herons(a,b,c)}")
        break
    except ValueError as e:
        print(f"Error: {e}")

# Method - 2

while True:
    try:
        a,b,c = map(float,input("Enter the three sides of Triangle: ").split())
        Area = round(0.25*((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))**(1/2),8)
        if Area <= 0:
            raise ValueError()
        print(f"Area: {Area}")
        break
    except:
        print("The given sides does not form a Triangle\n")


