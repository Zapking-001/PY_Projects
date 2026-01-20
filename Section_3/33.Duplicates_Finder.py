"""
Docstring for 33.Duplicates Finder: This program lists out which objects has Duplicates present in the list

        Efficiency: Time complexity is O(n)
                    Space complexity is O(n)
                    Where n is the length of the string.

"""
def find_duplicates(arr):
    freq = {}
    duplicates = []
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    for key, val in freq.items():
        if val > 1:
            duplicates.append(key)
    return duplicates

ls = input("Enter the objects: ").split()

print(f"Duplicates are present for: {",".join(map(str, find_duplicates(ls)))}")