"""
Docstring for 37.Check_Sorted: This program focuses on Sorted List / Array. Through this program, we can know if the list is sorted or not.

        Efficiency: Time complexity is O(n)
                    Space complexity is O(1)
"""
# Method - 1
ls = input("Enter the objects: ").split()

def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

if is_sorted(ls):
    print("The list is sorted.")
else:
    print("The list is not sorted.")

# Method - 2

print("The list is sorted." if sorted(input("Enter the objects: ").split()) == input("Enter the objects: ").split() else "The list is not sorted.")