"""
Docstring for 65.Volume_Sphere: 

                Formula: 
                         Volume = _4_ πR³
                                   3

                Efficiency : Time complexity: O(1)
                             Space complexity: O(1)
                
"""

# Method - 1
import math as m
r = float(input("Enter the radius: "))
def sphere_volume(radius):
    return (4/3) * m.pi * (radius**3)

print(f"Volume: {sphere_volume(r):.2f}")

# Method - 2
r = float(input("Enter the radius: "))
print(f"Volume: {round((4/3) * m.pi * (r**3),2)}")

# Method - 3
def sphere_volume_mathematical():
    radius = float(input("Radius: "))
    
    pi_approx = 3.141592653589793
    
    radius_cubed = radius * radius * radius
    
    volume = (4 / 3) * pi_approx * radius_cubed
    
    print("Volume:", volume)

sphere_volume_mathematical()