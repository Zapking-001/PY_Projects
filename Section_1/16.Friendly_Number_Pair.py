"""
Docstring for 16.Friendly_Number_Pair: Two numbers are called friendly numbers (or amicable numbers) if they share the same abundance index.
                                        Abundance Index : ∑di/n

6 → Divisors: 1, 2, 3, 6 → Sum = 12
Abundance Index = 12/6=2

28 → Divisors: 1, 2, 4, 7, 14, 28 → Sum = 56
Abundance Index = 56/28=2


            Efficiency: Time complexity = O(√n + √m)
                        Space complexity = O(1)

"""
def sum_of_divisors(n):
    return sum(d for d in range(1, n+1) if n % d == 0)

def abundance_index(n):
    return sum_of_divisors(n) / n

def are_friendly(a, b):
    return abundance_index(a) == abundance_index(b)

m,n = map(int,input("Enter the first number: ").split())

if are_friendly(m,n):
    print(f"{m} and {n} are friendly numbers.")
else:
    print(f"{m} and {n} are not friendly numbers.")