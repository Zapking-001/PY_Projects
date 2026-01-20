"""
Docstring for 27.Substring Search: This program focuses to search for any substring in The Main string? And if yes it woul+d return the index

        Efficiency: Time complexity is O(n + m)
                    Space complexity is O(m)
                    Where n is the length of the string.

"""
def manual_substring_search(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            return i
    return -1 

str1, str2 = input("Enter the Primary String: "), input("Enter the Search string: ")

index = manual_substring_search(str1, str2)

if index != -1:
    print(f"Substring '{str2}' found at index {index} in '{str1}'.")
else:
    print(f"The Search failed or No result found.")