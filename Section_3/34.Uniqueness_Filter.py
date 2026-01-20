"""
Docstring for 34.Uniqueness_Filter: This program focuses on a given list and returns a new list with only the unique elements (remove duplicates).
        There are many ways for performing this task, I prefer the dict.fromkeys() method, which works for Python verse ≥ 3.7 {Method-3}


        Efficiency: Time complexity is O(n)
                    Space complexity is O(n)
                    Where n is the length of the string.
    
"""

ls = input("Enter the objects: ").split()

# Method 1
def unique_elements(arr):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result


print(f"Unique List: {unique_elements(ls)}")

# Method 2

'''def uniquing(arr):
    return list(set(arr))

print(f"Unique List: {uniquing(ls)}")'''

# Method 3

'''print(list(dict.fromkeys(ls)))'''
