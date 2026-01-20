"""
Docstring for 64.Harmonic_displacement: 
            Formula: 
                        y(t) = Asin(ωt+φ)
                        ω = √(k/m)

            Efficiency : Time complexity: O(1)
                         Space complexity: O(1)

          User Guide Ex: A = 2
                         ω = 0.5
                         φ = 0
                         t = 4
                        You are modeling a pendulum with an amplitude of 2 meters. 
                        It swings with an angular frequency of 0.5 rad/s.
                        You want to find its position at 4 seconds.
                        Assuming it started from the equilibrium point, φ = 0).

"""

# Method - 1
import math

def shm_E():
    try:
        a = float(input("Enter Amplitude (A): "))
        ω = float(input("Enter Angular Frequency (w): "))
        φ = float(input("Enter Phase Constant in radians (φ): "))
        t = float(input("Enter Time (t): "))

        displacement = a * math.sin(ω * t + φ)
        
        print(f"Output: Displacement x({t}) = {displacement:.4f}")
            
    except ValueError:
        print("Invalid input. Please enter numerical values.")

shm_E()

# Method - 2
import math
def shm_s():
    a, w, p, t = map(float, input("Enter A, w, φ, t: ").split())
    print(f"x: {a * math.sin(w * t + p):.4f}")
shm_s()

# Method - 3
def shm_mathematical():
    a = float(input("Amplitude: "))
    ω = float(input("Angular Frequency: "))
    φ = float(input("Phase: "))
    t = float(input("Time: "))

    # Calculate the angle (theta)
    theta = (ω * t) + φ

    # Normalize theta to be within -π to π for better Taylor accuracy
    # Using 3.14159 as a manual π constant
    π = 3.141592653589793
    theta = theta % (2 * π)
    if theta > π:
        theta -= 2 * π

    # Taylor Series for sin(x) with 10 terms for precision
    def manual_sin(x):
        term = x
        sin_x = x
        for n in range(1, 15):
            # Calculate (-1)^n * x^(2n+1) / (2n+1)!
            term *= -1 * x * x / ((2 * n) * (2 * n + 1))
            sin_x += term
        return sin_x

    displacement = a * manual_sin(theta)
    print("Displacement:", displacement)