"""
Docstring for 79.Vectors

                Efficiency: Time complexity = O(dim)
                            Space complexity = O(1)
"""
# Method - 1
import math

def vector_ops_efficient(u, v):
    sum_sq_u = 0
    sum_sq_v = 0
    dot_prod = 0
    
    for i in range(len(u)):
        sum_sq_u += u[i]**2
        sum_sq_v += v[i]**2
        dot_prod += u[i] * v[i]
        
    mag_u = math.sqrt(sum_sq_u)
    mag_v = math.sqrt(sum_sq_v)
    
    # Angle in radians: cos(theta) = (u . v) / (|u| * |v|)
    angle = math.acos(dot_prod / (mag_u * mag_v)) if mag_u * mag_v != 0 else 0
    
    return mag_u, dot_prod, angle

#------------------------------------------------------------------------------------------#

# Method - 2

import math

def s_vector(u, v):
    dot = sum(a*b for a, b in zip(u, v))
    mag = lambda vec: math.sqrt(sum(x**2 for x in vec))
    angle = math.acos(dot / (mag(u) * mag(v)))
    return mag(u), dot, angle

#------------------------------------------------------------------------------------------#

# Method - 3
import math

def vector_math(u, v):
    # Magnitude formula: sqrt of sum of squares
    mag_u = math.sqrt(sum(ui**2 for ui in u))
    mag_v = math.sqrt(sum(vi**2 for vi in v))
    
    # Dot product: sum of product of components
    dot_product = sum(u[i] * v[i] for i in range(len(u)))
    
    # Angle calculation via inverse cosine
    cos_theta = dot_product / (mag_u * mag_v)
    # Clamp value to [-1, 1] to avoid floating point errors for acos
    angle_rad = math.acos(max(-1, min(1, cos_theta)))
    
    return {
        "Magnitude_U": mag_u,
        "Dot_Product": dot_product,
        "Angle_Radians": angle_rad
    }

# Example Usage
u = list(map(float, input("Enter components for vector u (space-separated): ").split()))
v = list(map(float, input("Enter components for vector v (space-separated): ").split()))

# Ensure vectors have the same dimension
if len(u) != len(v):
    print("Error: Vectors must have the same dimension.")
else:
    mag_u_eff, dot_prod_eff, angle_eff = vector_ops_efficient(u, v)
    print(f"\nEfficient Method:")
    print(f"  Magnitude of u: {mag_u_eff:.4f}")
    print(f"  Dot Product (u . v): {dot_prod_eff:.4f}")
    print(f"  Angle between u and v (radians): {angle_eff:.4f}")

    mag_u_short, dot_prod_short, angle_short = s_vector(u, v)
    print(f"\nShort Method:")
    print(f"  Magnitude of u: {mag_u_short:.4f}")
    print(f"  Dot Product (u . v): {dot_prod_short:.4f}")
    print(f"  Angle between u and v (radians): {angle_short:.4f}")

    math_results = vector_math(u, v)
    print(f"\nMathematical Method:")
    print(f"  Magnitude of u: {math_results['Magnitude_U']:.4f}")
    print(f"  Dot Product (u . v): {math_results['Dot_Product']:.4f}")
    print(f"  Angle between u and v (radians): {math_results['Angle_Radians']:.4f}")