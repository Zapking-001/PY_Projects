"""
Docstring for 6.Find the Divisors: This program helps us to get our Divisors.
                Rule: Return {d | d | n}; iterate d ≤ √n and add d and n/d to the list.

                Efficiency: Time complexity is O(√n)
                            Space complexity is O(d)
"""
def num_of_divisors(k):
    if k <= 0:
        return 0
    count = 0
    for i in range(1, k + 1):
        if k % i == 0:
            count += 1
    return count
def display_divisors(k):
    if k <= 0:
        return
    print(f"The divisors of {k} are:", end=" ")
    for i in range(1, k + 1):
        if k % i == 0:
            print(i, end=" ")
    print()

n = int(input("Enter the number: "))
while True:
    try:
        choice = input("Do you want to say the Number of Divisors or to List the Divisors or Both?\nAns: ")
        if choice.upper() == 'N':
            print(f"The number of divisors of {n} is {num_of_divisors(n)}")
            break
        elif choice.lower() == 'l':
            display_divisors(n)
            break
        elif choice.capitalize() == 'B':
            print(f"The number of divisors of {n} is {num_of_divisors(n)}")
            display_divisors(n)
            break
        else:
            raise ValueError()
    except:
        print("\nPlease enter a valid input, either 'N' or 'L' or 'B'\n")