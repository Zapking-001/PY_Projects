"""
Docstring for 36.Rotation_Of_String: Core Logic = new index=(i+k) mod n
        Efficiency: Time complexity is O(n)
                    Space complexity is O(1)
                    Where n is the number of elements in the list.



"""

ls,key = input("Enter the objects: ").split() , int(input("Enter the key to be rotated: "))
# Method - 1
def rotate_list_inplace(arr, k):
    n = len(arr)
    k %= n
    arr[:] = arr[-k:] + arr[:-k]
    return arr
 
print(f"Original List: {ls}\nRotated List: {rotate_list_inplace(ls, key)}\n\n")

# Method - 2
print(f"Original List: {ls}\nRotated List: {ls[-(key%(len(ls))):] + ls[:-(key%(len(ls)))]}")