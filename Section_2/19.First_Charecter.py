"""
Docstring for 19.First_Charecter : This program focuses on return the first Charecter in the string which is not repeating

        Ex: In the term " SWISS" ; S repeats, W & I doesn't repeat but W is the first charecter, so we return it.
        
        Efficiency: Time complexity is O(n)
                    Space complexity is O(1)
                    Where n is the length of the string.
"""
def first_non_repeating_char(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None

S = input("Enter a string: ")
result = first_non_repeating_char(S)
if result:
    print(f"The first non-repeating character in '{S}' is '{result}'.")
else:
    print(f"There are no such Non-Repeating characters in '{S}'.")