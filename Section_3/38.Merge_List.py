"""
Docstring for 38.Merge_List: This program focuses to merge two Sorted Lists
    
    Task: To make the code Efficient, which means that the runtime-complexity must be Less, than expected. { Method - 1 does it }

        Efficiency: Time complexity is O(n + m)
                    Space complexity is O(1)

"""
# Method - 1

def merge_sorted(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:]); result.extend(b[j:])
    return result

ls1, ls2 = input("Enter the objects in List_1: ").split(), input("Enter the objects in List_2: ").split()

print(f"Merged List: {merge_sorted(ls1, ls2)}")

# Method - 2

print(f"Merged List: {sorted(input("Enter the objects in List_1: ").split() + input("Enter the objects in List_2: ").split())}")