"""
Docstring for 35.Second_Largest: This program uses the time complexity efficiently One-pass solution → efficient O(n), and returns the second Largest element in the list. Provided the elements are Numbers

        Efficiency: Time complexity is O(n)
                    Space complexity is O(1)
                    n is the number of elements in the list.


"""

ls = input("Enter the objects: ").split()

def second_largest(arr):
    if len(arr) < 2:
        return None
    
    max1 = max2 = float('-inf')
    
    for x in arr:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2 and x != max1:
            max2 = x
    
    return max2 if max2 != float('-inf') else None


print(f"Second largest element: {second_largest(ls)}")