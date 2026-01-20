"""
Docstring for 44.Missing_letter

            Efficiency : Time complexity: O(n)
                         Space complexity: O(1)
                         
"""

ls = input("Give the sum to N or the list of numbers in any order, but should be from 1 to N: ").split()
n = int(input("Enter the value of N: "))

missing = n*(n+1)//2 - sum(map(int, ls))

while True:
    try:
        if missing<= n:
            print(f"Missing number is: {missing}")
            break
        else:
            raise ValueError
    except:
        print("Invalid sum or list of numbers.")
        print("\nWhy Failed?")
        print("Ans: If the list is provided then")
    