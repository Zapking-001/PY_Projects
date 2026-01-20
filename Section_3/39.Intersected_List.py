"""
Docstring for 39.Intersected_List : This program returns the common elements / objects from the 2 sorted lists

            Efficiency : Time complexity: O(m+n)
                         Space complexity: O(min(n,m))
"""

ls1, ls2 = input("Enter the objects in List_1: ").split(), input("Enter the objects in List_2: ").split()

# Method - 1
def list_intersection(list1, list2):
    return list(set(list1) & set(list2))

print(f"Intersected List: {sorted(list_intersection(ls1, ls2))}")

# Method - 2

print(f"The similar elements are: {sorted(list(set(ls1) & set(ls2)))}")
