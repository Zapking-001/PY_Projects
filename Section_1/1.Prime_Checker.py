"""
Docstring for 1.Prime_Checker : n > 1 is prime iff ∀ k ∈ {2,...,⌊√n⌋}, n ̸≡ 0 (mod k).

                Efficiency: Time complexity is O(√n)
                            Space complexity is O(1)

"""
# Method - 1
def is_prime_efficient(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    
#-----------------------------------------------------#

# Method - 2

def is_prime_short(n):    return n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))

#-----------------------------------------------------#

# Method - 3

def is_prime(n):
    if n <= 1:
        return False
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            return False
    return True


n = int(input("Enter the number: "))
if is_prime_efficient(n):
    print(f"{n} is a prime number (Efficient).")
else:
    print(f"{n} is not a prime number (Efficient).")

if is_prime_short(n):
    print(f"{n} is a prime number (Short).")
else:
    print(f"{n} is not a prime number (Short).")

if is_prime(n):
    print(f"{n} is a prime number (Mathematical).")
else:
    print(f"{n} is not a prime number (Mathematical).")