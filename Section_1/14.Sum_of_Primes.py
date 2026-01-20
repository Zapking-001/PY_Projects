"""
Docstring for 14.Sum of Primes upto N,

        Ex: N = 10 → Primes: 2, 3, 5, 7 → Sum = 17
        
        Efficiency: Time complexity = O(N log log N)
                    Space complexity = O(N)

"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(N):
    return sum(i for i in range(2, N+1) if is_prime(i))

n = int(input("Enter the number N: "))

print(f"Sum of all Primes upto {n} = {sum_of_primes(n)}")