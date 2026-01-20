"""
Docstring for 68.GP_genre

            Efficiency : Time complexity: O(n)
                         Space complexity: O(1)

"""

#
# Method - 1
def geometric_progression(a, r, n):
    """
    Calculates the nth term and sum of a geometric progression.

    Args:
        a (float): The first term.
        r (float): The common ratio.
        n (int): The number of terms.

    Returns:
        tuple: A tuple containing the nth term and the sum of the first n terms.
    """
def gp_efficient(a, r, n):
    curr = a
    for _ in range(n):
        yield curr
        curr *= r

# Example: list(gp_efficient(3, 2, 5)) -> [3, 6, 12, 24, 48]

#-----------------------------------------------------#

# Method - 2
def gp_short(a, r, n):
    return [a * r**i for i in range(n)]

# Example: gp_short(3, 2, 5) -> [3, 6, 12, 24, 48]

#-----------------------------------------------------#

# Method - 3
def gp_math(a, r, n):
    # Calculates each term using the explicit formula a * r^k
    return [a * pow(r, k) for k in range(n)]

# Example: gp_math(3, 2, 5) -> [3, 6, 12, 24, 48]



# Example usage
a = float(input("Enter the first term (a): "))
r = float(input("Enter the common ratio (r): "))
n = int(input("Enter the number of terms (n): "))

nth_term, sum_n_terms = geometric_progression(a, r, n)

if nth_term is not None:
    print(f"The {n}th term is: {nth_term}")
    print(f"The sum of the first {n} terms is: {sum_n_terms}")
else:
    print("Number of terms (n) must be positive.")

#-----------------------------------------------------#

print(list(gp_efficient(a, r, n)))
print(gp_short(a, r, n))
print(gp_math(a, r, n))

#-----------------------------------------------------#